from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from rsvp.themes.models import Theme
from django.utils import timezone


class DianaRoss(models.Model):
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    site_url = models.SlugField(unique=True,
                                help_text='Your birthday invitation url. e.g. reservasidulu.com/undangan-anak-mantan')

    title = models.CharField(max_length=40, help_text='Your birthday title')
    subtitle = models.CharField(max_length=40, help_text='Your birthday subtitle')
    img_background = models.ImageField(upload_to='img/diana_ross/', blank=True)
    about_img = models.ImageField(upload_to='img/diana_ross/', blank=True, help_text='Your summary image')
    about_title = models.CharField(blank=False, max_length=30, help_text='Your summary brief title')
    about = models.TextField(blank=False, help_text='Your summary brief')
    data_places_brief = models.TextField(blank=False, help_text='Explain where\'s your birthday will looks like')
    big_date = models.CharField(max_length=2, help_text='Day, e.g. 02')
    month_and_year = models.CharField(max_length=7, help_text='Month and Year (e.g. 09.1945)')
    start_from = models.CharField(max_length=20, help_text='Start from')
    place_image = models.ImageField(upload_to='img/places/', blank=False)
    place = models.CharField(max_length=100, help_text='Your birthday places')
    short_msg_img = models.ImageField(upload_to='img/diana_ross/', blank=False)
    short_message = models.CharField(max_length=100, help_text='Your additional information, e.g. <b>no child</b>')
    gallery1 = models.ImageField(blank=True, upload_to='img/diana_ross/', help_text='Your gallery')
    gallery2 = models.ImageField(blank=True, upload_to='img/diana_ross/', help_text='Your gallery')
    gallery3 = models.ImageField(blank=True, upload_to='img/diana_ross/', help_text='Your gallery')
    gallery4 = models.ImageField(blank=True, upload_to='img/diana_ross/', help_text='Your gallery')
    gallery5 = models.ImageField(blank=True, upload_to='img/diana_ross/', help_text='Your gallery')
    gallery6 = models.ImageField(blank=True, upload_to='img/diana_ross/', help_text='Your gallery')
    gallery7 = models.ImageField(blank=True, upload_to='img/diana_ross/', help_text='Your gallery')
    gallery8 = models.ImageField(blank=True, upload_to='img/diana_ross/', help_text='Your gallery')
    gallery9 = models.ImageField(blank=True, upload_to='img/diana_ross/', help_text='Your gallery')

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
        return reverse('diana_ross_detail', kwargs={'site_url': self.site_url})

