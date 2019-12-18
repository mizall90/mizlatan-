from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse_lazy, reverse
from django.core.exceptions import PermissionDenied

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.db.models import Q

from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView

from .models import Event, EventRegistration, Venue
from .forms import EventCreateForm, EventRegistrationForm, VenueCreateForm
#from emailtemplate.models import EmailTemplate

from datetime import datetime
from django.utils import timezone
from .mixins import PermissionMixin
from web.forms import JunkiriForm
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.


class EventList(ListView):
    model = Event
    template_name = 'event/list.html'
    context_object_name = 'events'
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.filter(end_date__gt=timezone.now())

    def get_context_data(self, **kwargs):
        context = super(EventList, self).get_context_data(**kwargs)
        context['past_events'] = self.model.objects.filter(end_date__lte=timezone.now())

        return context

class EventDetail(DetailView):
    model = Event
    template_name = 'event/detail.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super(EventDetail, self).get_context_data(**kwargs)
        past_events = self.model.objects.filter(end_date__lte=timezone.now())
        context['past_events'] = past_events.values_list('id', flat=True)
        return context


class Registration(CreateView):
    model = EventRegistration
    form_class = EventRegistrationForm
    template_name = 'event/event_register.html'
    success_url = reverse_lazy('event_list')

    def get(self, request, *args, **kwargs):
        registration = super(Registration, self).get(request, *args, **kwargs)
        user = self.request.user
        event = Event.objects.get(id=self.kwargs['event_id'])
        past_events = Event.objects.filter(end_date__lte=timezone.now())
        past_event = past_events.filter(start_date__lt=datetime.today()).values_list('id', flat=True)
        
        if event.id in past_event:
            messages.error(request, 'Registration have been closed for this event')
            raise PermissionDenied() #or Http404

        attend_list = event.get_attendees()
        if user.is_authenticated():
            if user.id in attend_list:
                messages.error(request, 'You are already in waiting list for this event.')
                raise PermissionDenied() #or Http404
        
        total_attendees = event.total_attendees()
        if event.registration_limit == total_attendees:
            messages.error(request, 'Registration is full for this event.')
            raise PermissionDenied() #or Http404
        return registration
    
    def get_initial(self):
        try:
            attendee = User.objects.get(username=self.request.user)
        except:
            attendee = None

        initial = super(Registration, self).get_initial()
        if attendee != None:
            initial['name'] = attendee.username
            initial['email_address'] = attendee.email
        return initial

    def get_form_kwargs(self):
        kwargs = super(Registration, self).get_form_kwargs()
        kwargs['event_id'] = self.kwargs['event_id']
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.event_id = self.kwargs['event_id']

        # dietery req
        Vegan = self.request.POST.get('dietery_requirements_Vegan')
        Vegetarian = self.request.POST.get('dietery_requirements_Vegetarian')
        Kosher = self.request.POST.get('dietery_requirements_Kosher')
        Allergic = self.request.POST.get('dietery_requirements_Allergic')
        Lactose = self.request.POST.get('dietery_requirements_Lactose')
        Non = self.request.POST.get('dietery_requirements_None')
        Others = self.request.POST.get('others')
        print(Vegan)
        print(Vegetarian)
        print(Kosher)
        print(Allergic)
        print(Lactose)
        print(Non)
        print(Others)

        regs = form.save(commit=False)

        diet = [Vegan, Vegetarian, Kosher, Allergic, Lactose, Non]
        if any(option for option in diet):
            req = ''
            for d in diet:
                if not d == None:
                    req += d + ', ' 
                else:
                    continue
            req = req
            regs.dietery_requirements = req
        else:
            regs.dietery_requirements = Others
        regs.save()

        # sending mail
        context_data = {
            "event" : form.cleaned_data['event'], 
            "nuid" : form.cleaned_data['nuid'], 
            "name" : form.cleaned_data['name'], 
            "registration_type" : form.cleaned_data['registration_type'], 
            "department" : form.cleaned_data['department'], 
            "region" : form.cleaned_data['region'], 
            "email_address" : form.cleaned_data['email_address'], 
            "mobile_phone" : form.cleaned_data['mobile_phone'], 
            "dietery_requirements" : form.cleaned_data['dietery_requirements'], 
            "comments" : form.cleaned_data['comments'],
            "user" : form.cleaned_data['user'], 
        }
        #self.notify_wait(context_data)
        messages.success(self.request, 'You are now on waitinglist for event {0}'.format(context_data.get('event')))

        return super(Registration, self).form_valid(form)

    def get_success_url(self):
        return reverse('event_detail', args=(self.kwargs['event_id'],))
    
    def get_context_data(self, **kwargs):
        context = super(Registration, self).get_context_data(**kwargs)
        user = self.request.user
        context['event_value'] = Event.objects.get(id=self.kwargs['event_id'])
        if user.is_authenticated():
            context['event_user'] = User.objects.get(id = user.id)
        return context
    
    # def notify_wait(self, context_data):
    #     subject, body = EmailTemplate.get_email_string(settings.TEMPLATE_WAIT, context_data)
    #     send_mail(
    #         subject=subject,
    #         message=body,
    #         from_email=settings.DEFAULT_ADMIN_EMAIL,
    #         recipient_list=[context_data.get('email_address')],
    #         html_message=body
    #     )
    

class ConfirmRegistration(LoginRequiredMixin, DetailView):
    model = EventRegistration
    def dispatch(self, request, *args, **kwargs):
        super(ConfirmRegistration, self).dispatch(request, *args, **kwargs)
        self.object = self.get_object()
        obj = self.object

        if obj.status != 'confirm':
            obj.status = 'confirm'
            obj.save()

            # sending mail
            context_data = {
                "event" : obj.event, 
                "nuid" : obj.nuid, 
                "name" : obj.name, 
                "registration_type" : obj.registration_type, 
                "department" : obj.department, 
                "region" : obj.region, 
                "email_address" : obj.email_address, 
                "mobile_phone" : obj.mobile_phone, 
                "dietery_requirements" : obj.dietery_requirements, 
                "comments" : obj.comments,
                "user" : obj.user, 
            }
            #self.notify_confirm(context_data)
            messages.success(self.request, 'Event {0} has been confirmed for {1}'.format(obj.event.title, obj.name))

        return redirect("/admin/event/eventregistration/")
    
    # def notify_confirm(self, context_data):
    #     subject, body = EmailTemplate.get_email_string(settings.TEMPLATE_CONFIRM, context_data)
    #     send_mail(
    #         subject=subject,
    #         message=body,
    #         from_email=settings.DEFAULT_ADMIN_EMAIL,
    #         recipient_list=[context_data.get('email_address')],
    #         html_message=body
    #     )

class DeclineRegistration(LoginRequiredMixin, DetailView):
    model = EventRegistration
    def dispatch(self, request, *args, **kwargs):
        super(DeclineRegistration, self).dispatch(request, *args, **kwargs)
        self.object = self.get_object()
        obj = self.object

        if obj.status != 'decline':
            obj.status = 'decline'
            obj.save()

            # sending mail
            context_data = {
                "event" : obj.event, 
                "nuid" : obj.nuid, 
                "name" : obj.name, 
                "registration_type" : obj.registration_type, 
                "department" : obj.department, 
                "region" : obj.region, 
                "email_address" : obj.email_address, 
                "mobile_phone" : obj.mobile_phone, 
                "dietery_requirements" : obj.dietery_requirements, 
                "comments" : obj.comments,
                "user" : obj.user, 
            }
            #self.notify_decline(context_data)
            messages.success(self.request, 'Event {0} has been declined for {1}'.format(obj.event.title, obj.name))
        return redirect("/admin/event/eventregistration/")

    # def notify_decline(self, context_data):
    #     subject, body = EmailTemplate.get_email_string(settings.TEMPLATE_TDECLINE, context_data)
    #     send_mail(
    #         subject=subject,
    #         message=body,
    #         from_email=settings.DEFAULT_ADMIN_EMAIL,
    #         recipient_list=[context_data.get('email_address')],
    #         html_message=body
    #     )


class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventCreateForm
    template_name = 'event/event_create.html'
    success_url = reverse_lazy('event_list')

    def get_form_kwargs(self):
        kwargs = super(EventCreate, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super(EventCreate, self).get_context_data(**kwargs)
        return context
    

class EventUpdate(PermissionMixin, UpdateView):
    model = Event
    form_class = EventCreateForm
    success_url = reverse_lazy('event_list')
    template_name = 'event/update_form.html'
    template_name_suffix = '_update_form'
    success_message = "%(title)s was updated successfully"

    def get_form_kwargs(self):
        kwargs = super(EventUpdate, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EventDelete(PermissionMixin, DeleteView):
    model = Event
    template_name = 'event/delete.html'
    success_url = reverse_lazy('event_list')
    context_object_name = 'event'
    success_message = "%(title)s was deleted successfully"

    # def get_object(self, *args, **kwargs):
    #     event = super(EventDelete, self).get_object(*args, **kwargs)
    #     if event.creator != self.request.user:
    #         raise Http404() #or Http404
    #     return event

class EventRegister(LoginRequiredMixin, CreateView):
    model = EventRegistration
    form_class = EventRegistrationForm
    template_name = 'event/event_register.html'


class VenuDetailView(DetailView):
    model =  Venue
    template_name = 'event/venue.html'
    context_object_name = 'venue'

class VenueCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Venue
    form_class = VenueCreateForm
    template_name = 'event/venue_create.html'
    success_url = reverse_lazy('dash')
    success_message = "Venue successfully created!"
    
    def get_context_data(self, **kwargs):
        context = super(VenueCreate, self).get_context_data(**kwargs)
        return context
    