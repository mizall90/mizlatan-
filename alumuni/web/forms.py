from django import forms
from .models import Junkiri, Team
from django.forms import ModelForm
from django.utils import timezone
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from django_summernote.widgets import (SummernoteWidget)    

class JunkiriForm(ModelForm):

    class Meta():
        model = Junkiri
        exclude = ('post_dt',)
        widgets = {
       'quote': SummernoteWidget(),
    }
        

   

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    message = forms.CharField(label='Message', widget=forms.Textarea)
    subject = forms.CharField(label='Subject', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    phone = forms.CharField(label='Phone', max_length=100)
