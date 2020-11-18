from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from rsvp.themes.models import Theme
from django.utils import timezone
from ckeditor.fields import RichTextField


class Aaron(models.Model):
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    site_url = models.SlugField(unique=True, default='Your wedding invitation url. e.g. reservasidulu.com/happy-dinosaur')

    # section 1
    title = models.CharField(max_length=40, help_text='Your birthday title')
    img_logo = models.CharField(max_length=100, default='Your title')
    about_name = models.CharField(max_length=30, default='Your name')
    about_age = models.CharField(max_length=10, default='1st')
    
    # section 2
    banner_subtitle = models.CharField(max_length=50, default='you are')
    banner_title = models.CharField(max_length=50, default='Eagerly Invited')
    banner_bg = models.ImageField(upload_to='img/aaron/', blank=True, null=True)
    banner_bg_mobile = models.ImageField(upload_to='img/aaron/', blank=True, null=True)
    
    # section 3
    about_image1 = models.ImageField(upload_to='img/aaron/', blank=True, null=True)
    about_image2 = models.ImageField(upload_to='img/aaron/', blank=True, null=True)
    about_image3 = models.ImageField(upload_to='img/aaron/', blank=True, null=True)
    about_image4 = models.ImageField(upload_to='img/aaron/', blank=True, null=True)
    about_image5 = models.ImageField(upload_to='img/aaron/', blank=True, null=True)
    about_image6 = models.ImageField(upload_to='img/aaron/', blank=True, null=True)
    about_image7 = models.ImageField(upload_to='img/aaron/', blank=True, null=True)
    about_image8 = models.ImageField(upload_to='img/aaron/', blank=True, null=True)
    about_image9 = models.ImageField(upload_to='img/aaron/', blank=True, null=True)
    about_image10 = models.ImageField(upload_to='img/aaron/', blank=True, null=True)
    
    # section 4
    dap_day = models.CharField(max_length=10, default='Sat')
    dap_date = models.CharField(max_length=30, default='18 April 2020')
    dap_time = models.CharField(max_length=30, default='18.00 PM')
    dap_place = models.CharField(max_length=30, default='Marina Village')
    dap_address = models.CharField(max_length=50, default='Baja Room 939 Quivira Way, San Diego California 92109')
    dap_dress = models.CharField(max_length=30, default='Colorful')
    
    # section 5
    inv_pdf = models.FileField(upload_to='file/aaron/', blank=True, null=True)

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
        return reverse('aaron_detail', kwargs={'site_url': self.site_url})
