from django.db import models
import datetime

# Create your models here.

POSITION_OPTIONS = (
      ('president', 'President'),
      ('vice president', 'Vice President'),
      ('outreach', 'Outreach'),
      ('Treasurer', 'Treasurer'),
      ('secretary', 'Secretary'),
      ('joint secretary', 'Joint Secretary')
   )

class Team(models.Model):
    first_name = models.CharField(blank=True, null=True, max_length=50)
    last_name = models.CharField(blank=True, null=True, max_length=50)
    position = models.CharField(choices=POSITION_OPTIONS, max_length=50, null=True, blank=True)
    batch = models.CharField(blank=True, null=True, max_length=50)
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(
       upload_to='profile/',
       verbose_name='Display Picture',
       blank=True, null=True, default="/profile/user.png")

    def __str__(self):
        return '%s' % self.first_name

class Junkiri(models.Model):
    photo = models.ImageField(blank=True, max_length=255, upload_to='Junkiri/%Y/%m', verbose_name='Junkiri Post') 
    post_title =  models.CharField(max_length=100, verbose_name='Title')
    author_name = models.CharField( max_length=50, verbose_name='Author Name')
    batch = models.CharField(max_length=50, verbose_name='Batch')
    quote = models.TextField(blank=True, null=True, verbose_name='Post Discription')
    post_dt = models.DateTimeField(blank=True, verbose_name='Post Date', default=datetime.datetime.now)
    is_starring = models.BooleanField(default=False, verbose_name='Star Post', help_text='Star Post will be shown on home page.')
    publish =  models.BooleanField(default=False, verbose_name='Publish', help_text='Latest 6 post that are marked publish will be shown on Junikiri list page.')
  
    def __str__(self):
        return '%s' % self.post_title

class Event(models.Model):
    event_dt = models.DateField(blank=True, null=True)
    event_title = models.CharField(blank=True, null=True, max_length=100)
    discription = models.TextField(blank=True, null=True) 
    co_ordinated_by =  models.ForeignKey(Team)
    banner = models.ImageField(
       upload_to='event/',
       verbose_name='Event Banner',
       blank=True, null=True)

    def __str__(self):
        return '%s' % self.event_title



