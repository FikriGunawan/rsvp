from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from rsvp.themes.models import Theme
from django.utils import timezone
from ckeditor.fields import RichTextField


class Anastasia(models.Model):
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    site_url = models.SlugField(unique=True, default='Your wedding invitation url. e.g. reservasidulu.com/pastel-party')

    # section 1
    title = models.CharField(max_length=40, help_text='Your birthday title')
    banner_name = models.CharField(max_length=30, default='Your name')
    banner_age = models.CharField(max_length=10, default='18th')
    
    # section 2
    banner_brief = models.TextField(default='Please join us in celebration of Anastasia’s birthday. It’s a party and you are cordially invited.')
    banner_bg = models.ImageField(upload_to='img/anastasia/', blank=True, null=True)
    banner_bg_mobile = models.ImageField(upload_to='img/anastasia/', blank=True, null=True)
    
    # section 3
    gallery_image1 = models.ImageField(upload_to='img/anastasia/', blank=True, null=True)
    gallery_image2 = models.ImageField(upload_to='img/anastasia/', blank=True, null=True)
    gallery_image3 = models.ImageField(upload_to='img/anastasia/', blank=True, null=True)
    gallery_image4 = models.ImageField(upload_to='img/anastasia/', blank=True, null=True)
    gallery_image5 = models.ImageField(upload_to='img/anastasia/', blank=True, null=True)
    
    # section 4
    dap_date = models.CharField(max_length=10, default='25.04.2020')
    dap_day = models.CharField(max_length=10, default='SAT')
    dap_time = models.CharField(max_length=20, default='5.30 PM')
    dap_place = models.CharField(max_length=40, default='Marina Village')
    dap_address = models.CharField(max_length=50, default='Baja Room 939 Quivira Way, San Diego California 92109')
    dap_dress = models.CharField(max_length=40, default='Wear black and white clothes')
    
    # section 5
    inv_pdf = models.FileField(upload_to='file/anastasia/', blank=True, null=True)

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
        return reverse('anastasia_detail', kwargs={'site_url': self.site_url})
