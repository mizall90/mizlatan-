from django.contrib import admin
from .models import Team, Junkiri
# from django_summernote.widgets import SummernoteModelAdmin
from django_summernote.admin import SummernoteModelAdmin
# from django.db import models

class JunkiriAdmin(SummernoteModelAdmin):
    model = Junkiri
    summernote_fields = ('quote',)
    

# class EventAdmin(SummernoteModelAdmin):
#     model = Event
#     summernote_fields = ('discription',)
   
class TeamAdmin(SummernoteModelAdmin):
    model = Team
    summernote_fields = ('text',)
   



admin.site.register(Team, TeamAdmin)

admin.site.register(Junkiri, JunkiriAdmin)

# admin.site.register(Event, EventAdmin)

