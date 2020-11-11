from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from rsvp.themes.models import Theme
from django.utils import timezone
from ckeditor.fields import RichTextField


class LiamFelicia(models.Model):
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    site_url = models.SlugField(unique=True,
                                default='Your wedding invitation url. e.g. reservasidulu.com/undangan-mantan')

    # section 1
    title = models.CharField(max_length=40, help_text='Your wedding title')
    bride_name = models.CharField(max_length=30, default='Your bride name')
    grome_name = models.CharField(max_length=30, default='Your gome name')
    hashtag = models.CharField(max_length=30, default='Your #hashtag here')
    img_logo = models.ImageField(upload_to='img/against/', blank=False, help_text='Your logo goes here')

    # section 2
    banner_bg = models.ImageField(upload_to='img/liam/', blank=True)
    banner_title = models.CharField(max_length=50, default='')
    section2_image = models.ImageField(upload_to='img/against/', blank=True, null=True, help_text='Your summary image')
    about_title = models.CharField(blank=False, max_length=200, help_text='Your summary brief title')
    about_brief = models.TextField(blank=False, help_text='Your summary brief')

    # section 3
    ceremony_date = models.CharField(max_length=100, default='Saturday, 22th July 2020')
    ceremony_time = models.CharField(max_length=100, default='3:00pm – 4:00pm')
    ceremony_place = models.TextField(default='New Faith Church '
                                              '415 Greenwich St (at Bethune St) New York, NY 10014 (212) 555–0123')

    reception_date = models.CharField(max_length=100, default='Saturday, 22th July 2020')
    reception_time = models.CharField(max_length=100, default='3:00pm – 4:00pm')
    reception_place = models.TextField(default='New Faith Church'
                                              '415 Greenwich St (at Bethune St) New York, NY 10014 (212) 555–0123')

    # section 4
    gallery1 = models.ImageField(blank=True, upload_to='img/against/', help_text='Your gallery')
    gallery2 = models.ImageField(blank=True, upload_to='img/against/', help_text='Your gallery')
    gallery3 = models.ImageField(blank=True, upload_to='img/against/', help_text='Your gallery')
    gallery4 = models.ImageField(blank=True, upload_to='img/against/', help_text='Your gallery')

    rsvp_img = models.ImageField(upload_to='img/against/', null=True)

    created = models.DateTimeField(auto_now_add=True, auto_created=True, editable=False)
    updated = models.DateTimeField(auto_created=True, auto_now=True, editable=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance = None

    def publish(self):
        self.published_date = timezone.now()

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('liam_detail', kwargs={'site_url': self.site_url})
