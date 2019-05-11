from django import forms
from .models import Junkiri, Event, Team
from django.forms import ModelForm
from django.utils import timezone


class JunkiriForm(ModelForm):

    class Meta():
        model = Junkiri
        exclude = ('post_dt',)

   

