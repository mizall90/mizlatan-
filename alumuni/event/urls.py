# # -*- coding: utf-8 -*-
from django.conf.urls import url,include
from django.contrib.auth.decorators import login_required

from .views import (EventList, EventDetail, Registration, ConfirmRegistration, DeclineRegistration, EventCreate, EventDelete, EventUpdate, VenuDetailView, VenueCreate
#  EventDelete, EventUpdate, EventCreate, EventRegister,
 )


urlpatterns = [
    url(r'^$', EventList.as_view(), name="event_list"),
    url(r'^(?P<pk>[\d]+)/$', EventDetail.as_view(), name="event_detail"),
    url(r'^venue/(?P<pk>[\d]+)/$', VenuDetailView.as_view(), name="event_venue"),
    url(r'^(?P<event_id>\d+)/register/$', Registration.as_view(), name='register'),
    url(r'^confirm/(?P<pk>[\d]+)/$', ConfirmRegistration.as_view(), name="confirm_event"),
    url(r'^decline/(?P<pk>[\d]+)/$', DeclineRegistration.as_view(), name="decline_event"),
    # url(r'^register/$', EventRegister.as_view(), name="add_attendees"),
    url(r'^create/$', EventCreate.as_view(), name="add_event"),
    url(r'^venue/create/$', VenueCreate.as_view(), name="add_venue"),
    url(r'^(?P<pk>[\d]+)/delete/', EventDelete.as_view(), name="delete_event"),
    url(r'^(?P<pk>[\d]+)/update/', EventUpdate.as_view(), name="update_event"),
]
