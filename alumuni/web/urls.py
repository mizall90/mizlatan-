from django.conf.urls import url, include
from . import views
from .views import ( IndexView, Junkiri_ListView, Junkiri_DetailView, Junkiri_Create, TeamView )
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^junkiri/$', Junkiri_ListView.as_view(), name='junkiri'),
    url(r'^junkiri/(?P<pk>[-\w]+)/$', Junkiri_DetailView.as_view(), name='junkiri-detail'),
    url(r'^create/$', Junkiri_Create.as_view(), name='junkiri_create'),
    url(r'^team/$', TeamView.as_view(), name='team'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)