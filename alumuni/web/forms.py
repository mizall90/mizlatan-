from django import forms
from .models import Junkiri, Event, Team
from django.forms import ModelForm
from django.utils import timezone


class JunkiriForm(ModelForm):

    class Meta():
        model = Junkiri
        exclude = ('post_dt',)

   

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    message = forms.CharField(label='Message', widget=forms.Textarea)
    subject = forms.CharField(label='Subject', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    phone = forms.CharField(label='Phone', max_length=100)


class EventForm(ModelForm):

    class Meta():
        model = Event
        fields = '__all__'
        