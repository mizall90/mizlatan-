from django.db import models
import datetime

# Create your models here.

POSITION_OPTIONS = (
    ('President', 'President'),
    ('Vice president', 'Vice President'),
    ('Outreach', 'Outreach'),
    ('Treasurer', 'Treasurer'),
    ('Secretary', 'Secretary'),
    ('Joint secretary', 'Joint Secretary')
)


class Team(models.Model):
    first_name = models.CharField(blank=True, null=True, max_length=50)
    last_name = models.CharField(blank=True, null=True, max_length=50)
    position = models.CharField(
        choices=POSITION_OPTIONS, max_length=50, null=True, blank=True)
    batch = models.CharField(blank=True, null=True, max_length=50)
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to='profile/',
        verbose_name='Display Picture',
        blank=True, null=True, default="/profile/user.png")

    def __str__(self):
        return '%s' % self.first_name


class Junkiri(models.Model):
    photo = models.ImageField(blank=True, max_length=255,
                              upload_to='Junkiri/%Y/%m', verbose_name='Junkiri Post')
    post_title = models.CharField(max_length=100, verbose_name='Title')
    author_name = models.CharField(max_length=50, verbose_name='Author Name')
    batch = models.CharField(max_length=50, verbose_name='Batch')
    quote = models.TextField(blank=True, null=True,
                             verbose_name='Post Discription')
    post_dt = models.DateTimeField(
        blank=True, verbose_name='Post Date', default=datetime.datetime.now)
    is_starring = models.BooleanField(
        default=False, verbose_name='Star Post', help_text='Star Post will be shown on home page.')
    publish = models.BooleanField(default=False, verbose_name='Publish',
                                  help_text='Latest 6 post that are marked publish will be shown on Junikiri list page.')

    # def starring(self, *args, **kwargs):
    #         articles = Junkiri.objects.all().exclude(pk=self.pk)
    #         if self.is_starring:
    #             for article in articles:
    #                 article.is_starring = False
    #                 article.save()
    #             super(Junkiri, self).save(*args, **kwargs)

    def __str__(self):
        return '%s' % self.post_title


# class Event(models.Model):
#     event_dt = models.DateTimeField(blank=True, null=True,verbose_name='Event start date.', help_text='Date should be in YYYY-MM-DD format i.e: 2011-11-11.')
#     event_end_dt = models.DateTimeField(blank=True, null=True,verbose_name='Event end date.', help_text='Date should be in YYYY-MM-DD format i.e: 2011-11-11.')
#     event_title = models.CharField(blank=True, null=True, max_length=100)
#     discription = models.TextField(blank=True, null=True)
#     co_ordinated_by = models.ForeignKey(Team)
#     banner = models.ImageField(
#         upload_to='event/',
#         verbose_name='Event Banner',
#         blank=True, null=True)
#     ended = models.BooleanField(default=False, verbose_name='End Event')
#     is_upcoming = models.BooleanField(
#         default=True, verbose_name="Upcoming Event")
#     is_ongoing = models.BooleanField(
#         default=False, verbose_name="Ongoing Event")

#     def save(self, *args, **kwargs):
#         if self.event_end_dt or self.is_ongoing:
#             self.is_upcoming = False
#             super(Event, self).save(*args, **kwargs)

#     def __str__(self):
#         return '%s' % self.event_title
