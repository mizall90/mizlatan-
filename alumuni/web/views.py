from django.shortcuts import render
from .models import Team, Junkiri, Event
from django.views.generic import TemplateView, ListView, DeleteView, DetailView, CreateView, FormView
from .forms import JunkiriForm
import datetime

# Create your views here.

class IndexView(TemplateView):
    template_name='home.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['teams'] = Team.objects.all()
        if Junkiri.objects.filter(is_starring=True):
            context['starring'] = Junkiri.objects.filter(is_starring=True).latest('post_dt')
        context['presedent'] = Team.objects.get(id=3)
        context['home'] = True
        return context


class Junkiri_Create(FormView):
    template_name = 'junkiri_form.html'
    form_class = JunkiriForm
    success_url='/junkiri'

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super().form_valid(form)
    

class Junkiri_ListView(ListView):
    template_name = 'junkiri_list.html'
    model = Junkiri

    def get_context_data(self, **kwargs):
        context = super(Junkiri_ListView, self).get_context_data(**kwargs) 
        context['Junkiri'] = Junkiri.objects.filter(publish=True).order_by('post_dt')
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