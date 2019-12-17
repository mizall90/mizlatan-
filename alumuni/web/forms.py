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


# class EventForm(ModelForm):

#     class Meta():
#         model = Event
#         fields = '__all__'
#         widgets = {
#         # 'start_date': DatePickerInput(), # default date-format %m/%d/%Y will be used
#         'discription': SummernoteWidget(),
#         'event_dt': DatePickerInput(format='%Y-%m-%d'), # specify date-frmat
#         'event_end_dt': DatePickerInput(format='%Y-%m-%d'), # specify date-frmat
#     }
        