from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from rsvp.themes.models import Theme
from django.utils import timezone
from ckeditor.fields import RichTextField


class FreeDianaRoss(models.Model):
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    site_url = models.SlugField(unique=True, default='Your birthday invitation url. e.g. reservasidulu.com/diana-ross')

    # section 1
    title = models.CharField(max_length=40, help_text='Your birthday title')
    name = models.CharField(max_length=30, default='Your name')
    hashtag = models.CharField(max_length=30, default='Your #hashtag here')
    
    # section 2
    image = models.ImageField(upload_to='img/free/diana_ross/', blank=True, null=True)
    image_mobile = models.ImageField(upload_to='img/free/diana_ross/', blank=True, null=True)
    date = models.CharField(max_length=2, default='23')
    month = models.CharField(max_length=2, default='09')
    year = models.CharField(max_length=4, default='2020')
    time = models.CharField(max_length=40, default='18.00 - Done')
    place = models.CharField(max_length=40, default='Hotel Mulia')
    place_image = models.ImageField(upload_to='img/free/diana_ross/', blank=True, null=True)
    address = models.CharField(max_length=40, default='Grand Ballroom')
    note = models.CharField(max_length=40, default='No Dolls, No Money')
    note_image = models.ImageField(upload_to='img/free/diana_ross/', blank=True, null=True)
    dress = models.CharField(max_length=40, default='All Pink')
    ct_date = models.ImageField(upload_to='img/free/diana_ross/', blank=True, null=True)
    ct_place = models.ImageField(upload_to='img/free/diana_ross/', blank=True, null=True)
    ct_note = models.ImageField(upload_to='img/free/diana_ross/', blank=True, null=True)
    
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
        return reverse('free_diana_ross_detail', kwargs={'site_url': self.site_url})
