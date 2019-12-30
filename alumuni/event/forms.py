from django.contrib.auth.models import User
from django import forms
from .models import Event, EventRegistration, Venue
from django_summernote.widgets import (SummernoteWidget)   
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput

class EventCreateForm(forms.ModelForm):
    #creator = forms.ModelChoiceField(queryset=User.objects.none(), widget=forms.Select(), empty_label=None, to_field_name="username", required=True)
    class Meta:
        model = Event
        fields = '__all__'
        # exclude = ('attachments',)
        widgets = {
        'description': SummernoteWidget(),
        'start_date': DatePickerInput(format='%Y-%m-%d', attrs={'placeholder': 'Event Start Date'}), # specify date-frmat
        'end_date': DatePickerInput(format='%Y-%m-%d', attrs={'placeholder': 'Event End Date'}), # specify date-format
        }
    def __init__(self, user, *args, **kwargs):
        super(EventCreateForm, self).__init__(*args, **kwargs)
        

class EventRegistrationForm(forms.ModelForm):
    event = forms.ModelChoiceField(queryset=Event.objects.none(), widget=forms.Select(), empty_label=None, to_field_name="title", required=True)
    user = forms.ModelChoiceField(queryset=User.objects.none(), widget=forms.Select(), empty_label=None, to_field_name="username", required=False)
    class Meta:
        model = EventRegistration
        # fields = '__all__'
        exclude = ('status',)
    
    def __init__(self, user, event_id, *args, **kwargs):
        super(EventRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['event'].queryset = Event.objects.filter(id = event_id)
        self.fields['user'].queryset = User.objects.filter(id = user.id)




class VenueCreateForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = '__all__'
        widgets = {
        'address': SummernoteWidget(),
        }