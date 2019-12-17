from django.contrib import admin
from django.utils.html import format_html
from django.core.urlresolvers import reverse

from django.db import models
from django_summernote.widgets import (SummernoteWidget)

# Register your models here.
from .models import (Venue, Event, EventRegistration)

class VenueAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'contact_number')
    
    
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'venue', 'start_date', 'end_date', 'attendee_list', )
    search_fields = ('title', 'description')
    ordering = ('-id',)

    formfield_overrides = {
        models.TextField: {'widget': SummernoteWidget},
    }

    def attendee_list(self, obj):
        return format_html("<a href='%s?event_id=%s'>Show</a>" % (
            reverse('admin:event_eventregistration_changelist'), obj.id))
    attendee_list.allow_tags = True
    attendee_list.short_description = 'Attendee List'

class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'nuid', 'user', 'email_address', 'custom_field', 'event', 'status', 'registration_actions', 'dietery_requirements')
    list_filter = ('status', 'event')
    search_fields = ('event', 'status')
    ordering = ('-id',)

    def custom_field(self, obj):
        return '{}'.format(obj.event.id)
    custom_field.short_description = 'Event Id'

    def registration_actions(self, obj):
        if obj.status == 'waiting':
            return format_html(
                '<a class="button" href="{}">Confirm</a>&nbsp;'
                '<a class="button" href="{}" style="background-color: red;">Decline</a>',
                reverse('confirm_event', args=[obj.pk]),
                reverse('decline_event', args=[obj.pk]),
            )
        elif obj.status == 'confirm':
            return format_html(
                '<a class="button" href="{}">Confirm</a>&nbsp;'
                '<a class="button" href="{}" style="background-color: red;">Decline</a>',
                reverse('confirm_event', args=[obj.pk]),
                reverse('decline_event', args=[obj.pk]),
            )
    registration_actions.short_description = 'Registration Actions'
    registration_actions.allow_tags = True



admin.site.register(Venue, VenueAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(EventRegistration, EventRegistrationAdmin)