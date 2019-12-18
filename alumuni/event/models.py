import uuid
from django.db import models
from django.conf import settings

from django.contrib.auth.models import User
from django_google_maps import fields as map_fields

GUESS_LIMIT = [(0, u"No limit")] + list(zip(range(1,100), range(1,100)))
STATUS_CHOICES = (
        ('waiting', 'Waiting'),
        ('confirm', 'Approved'),
        ('decline', 'Declined')
        )

REGISTRATION_TYPES = (
        ('person', 'Attend in Person'),
        ('remote', 'Attend via Remote')
        )

# Create your models here.
class EventBaseModel(models.Model):
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return '%s' % self.title




class Venue(EventBaseModel):
    title = models.CharField(max_length=200, unique=False)
    address = models.TextField(blank=True, null=True)
    contact_number = models.CharField(max_length=50, unique=False)
    # address = map_fields.AddressField(max_length=200)
    # geolocation = map_fields.GeoLocationField(max_length=100, blank=True, null=True)


class Event(EventBaseModel):
    title = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    # start_time = models.TimeField(help_text='Please use the following format: <em>HH:MM:SS<em>')
    # end_time = models.TimeField(help_text='Please use the following format: <em>HH:MM:SS<em>')
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    description = models.TextField(blank=True, help_text='Short description of event')

    attachments = models.FileField(upload_to='uploads/', blank=True)
    banner = models.ImageField(upload_to='event', blank=True, default="/static/img/bg.jpg", help_text='Image thumbnail for event.')

    duration = models.PositiveIntegerField(default=0, blank=True, help_text='Please use hours format for event duration.')
    registration_limit = models.IntegerField('Guest limit')

    class Meta:
        verbose_name = 'event'
        verbose_name_plural = 'events'
        ordering = ['start_date']
    
    def get_attendees(self):
        return self.eventregistration_set.values_list('user', flat=True)
    
    def total_attendees(self):
        return self.eventregistration_set.count()


class EventRegistration(EventBaseModel):
    event = models.ForeignKey(Event, verbose_name='Event')
    nuid = models.CharField(max_length=100, unique=False)
    name = models.CharField(max_length=15)
    registration_type = models.CharField(max_length=20, choices=REGISTRATION_TYPES, default='person', blank=True)
    department = models.CharField(max_length=15, default='', blank=True)
    region = models.CharField(max_length=15, default='', blank=True)
    email_address = models.EmailField(max_length=254, verbose_name='attendee email', help_text='email address of attendee')
    mobile_phone = models.CharField(max_length=15, default='', blank=True)
    dietery_requirements = models.TextField(null=True, default='', blank=True)
    comments = models.TextField(null=True, default='', blank=True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='waiting', blank=True)
    user = models.ForeignKey(User, verbose_name='Attendee', null=True, blank=True)

    def __str__(self):
        return self.event.title

    class Meta:
        verbose_name = 'Attendee for event'
        verbose_name_plural = 'Attendees for events'
        ordering = ['status', ]
        unique_together = (("event", "user"),("event", "email_address"),)
