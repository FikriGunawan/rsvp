from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from rsvp.themes.models import Theme
from django.utils import timezone
from ckeditor.fields import RichTextField


class DylanRose(models.Model):
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    site_url = models.SlugField(unique=True,
                                default='Your wedding invitation url. e.g. reservasidulu.com/bride-groom')

    # section 1
    title = models.CharField(max_length=40, help_text='Your wedding title')
    bride_name = models.CharField(max_length=30, default='Your bride name')
    grome_name = models.CharField(max_length=30, default='Your groom name')
    hashtag = models.CharField(max_length=30, default='Your #hashtag here')
    img_logo = models.ImageField(upload_to='img/dylan/', blank=True, help_text='Your logo goes here')
    img_background1 = models.ImageField(upload_to='img/dylan/', blank=True, null=True)

    # section 2
    story_image = models.ImageField(upload_to='img/dylan/', blank=True, null=True)
    story_brief = models.CharField(max_length=100, help_text='Your story goes here', null=True)

    # section 3
    section3_date1 = models.CharField(max_length=100, help_text='Your date and time', null=True)
    section3_place1 = models.TextField(null=True)
    section3_dresscode1 = models.CharField(max_length=40, null=True, blank=True)
    section3_image1 = models.ImageField(upload_to='img/dylan/', blank=True, null=True)

    section3_date2 = models.CharField(max_length=100, help_text='Your date and time', null=True)
    section3_place2 = models.TextField(default='')
    section3_dresscode2 = models.CharField(max_length=40, null=True)
    section3_image2 = models.ImageField(upload_to='img/dylan/', blank=True, null=True)

    # section 4
    accommodation = models.ImageField(upload_to='img/dylan/', blank=True, null=True)
    accommodation_text = models.TextField(default='')

    # section 5
    album_brief = models.TextField(blank=True, null=True)
    album1 = models.ImageField(upload_to='img/dylan/', blank=True, null=True)
    album2 = models.ImageField(upload_to='img/dylan/', blank=True, null=True)
    album3 = models.ImageField(upload_to='img/dylan/', blank=True, null=True)
    album4 = models.ImageField(upload_to='img/dylan/', blank=True, null=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance = None

    def publish(self):
        self.published_date = timezone.now()

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('dylan_detail', kwargs={'site_url': self.site_url})
