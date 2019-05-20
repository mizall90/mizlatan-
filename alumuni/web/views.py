from django.shortcuts import render
from .models import Team, Junkiri, Event
from django.views.generic import TemplateView, ListView, DeleteView, DetailView, CreateView, FormView
from .forms import JunkiriForm, ContactForm, EventForm
import datetime
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.contrib import messages


# Create your views here.

class IndexView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['teams'] = Team.objects.all()
        if Junkiri.objects.filter(is_starring=True):
            context['starring'] = Junkiri.objects.filter(
                is_starring=True).latest('post_dt')
        context['presedent'] = Team.objects.get(id=3)
        context['home'] = True
        context['contact_form'] = ContactForm
        context['events'] = Event.objects.all().exclude(ended=True).order_by('-event_dt')
        return context


class Junkiri_Create(FormView):
    template_name = 'junkiri_form.html'
    form_class = JunkiriForm
    success_url = '/junkiri'

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super().form_valid(form)


class Junkiri_ListView(ListView):
    template_name = 'junkiri_list.html'
    model = Junkiri

    def get_context_data(self, **kwargs):
        context = super(Junkiri_ListView, self).get_context_data(**kwargs)
        context['Junkiri'] = Junkiri.objects.filter(
            publish=True).order_by('post_dt')
        return context


class Junkiri_DetailView(DetailView):
    template_name = 'junkiri_detail.html'
    model = Junkiri
    context_object_name = "Junkiri"

    def get_context_data(self, **kwargs):
        context = super(Junkiri_DetailView, self).get_context_data(**kwargs)
        context['recent_posts'] = Junkiri.objects.all().order_by('-post_dt')[:4]
        return context


class TeamView(TemplateView):
    template_name = 'team.html'

    def get_context_data(self, **kwargs):
        context = super(TeamView, self).get_context_data(**kwargs)
        context['members'] = Team.objects.all()

        return context


class ContactView(FormView):
    template_name = 'contact_form.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        if form.is_valid() and self.request.method == 'POST':
            email_address = 'mizall90@gmail.com'
            name = self.request.POST.get('name', '')
            email = self.request.POST.get('email', '')
            subject = self.request.POST.get('subject', '')
            message = self.request.POST.get('message', '')
            phone_number = self.request.POST.get('phone', '')
            body = '''Name: %s
                        Contact No: %s
                        Email Address: %s
                        Subject: %s
                        Message: %s''' % (name, phone_number, email, subject, message)
            from_email = 'mizall90@gmail.com'
            send_mail('Recived Message', body, from_email, [email_address])
            messages.success(self.request, 'Thank you for contacting us.')
        return super().form_valid(form)



class Event_Create(FormView):
    template_name = 'event_form.html'
    form_class = EventForm
    success_url = '/event/list/'

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super().form_valid(form)

class EventList(ListView):
    template_name = 'event_list.html'
    model = Event

    def get_context_data(self, **kwargs):
        context = super(EventList, self).get_context_data(**kwargs)
        if Junkiri.objects.filter(is_starring=True):
            context['ongoing'] = Event.objects.filter(
                is_ongoing=True).latest('event_dt')
        context['events'] = Event.objects.filter(
            is_upcoming=True).order_by('-event_dt')
        context['pasts'] = Event.objects.filter(
            ended=True).order_by('-event_dt')
        return context
