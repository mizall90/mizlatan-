from django.contrib.auth.models import User
from django import forms
from .models import Event, EventRegistration

class EventForm(forms.ModelForm):
    creator = forms.ModelChoiceField(queryset=User.objects.none(), widget=forms.Select(), empty_label=None, to_field_name="username", required=True)
    class Meta:
        model = Event
        fields = '__all__'
    
    def __init__(self, user, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        if user.is_superuser:
            self.fields['creator'].queryset = User.objects.filter(id = user.id)



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