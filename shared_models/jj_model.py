from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from rsvp.themes.models import Theme
from django.utils import timezone
from ckeditor.fields import RichTextField


class JackJane(models.Model):
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    site_url = models.SlugField(unique=True, default='Your wedding invitation url. e.g. reservasidulu.com/bride-groom')

    # section 1
    title = models.CharField(max_length=40, default='Your wedding title')
    img_logo = models.ImageField(upload_to='img/jj/', blank=False, help_text='Your logo goes here')
    about_name2 = models.CharField(max_length=30, default='Your bride name')
    about_name1 = models.CharField(max_length=30, default='Your groom name')
    hashtag = models.CharField(max_length=30, default='Your #hashtag here')
    
    # section 2
    banner_date = models.CharField(max_length=10, default='27/05/20')
    banner_bg1 = models.ImageField(upload_to='img/jj/', blank=True, null=True)
    banner_bg2 = models.ImageField(upload_to='img/jj/', blank=True, null=True)
    banner_bg3 = models.ImageField(upload_to='img/jj/', blank=True, null=True)
    
    # section 3
    about_image1 = models.ImageField(upload_to='img/jj/', blank=True, null=True)
    about_place = models.CharField(max_length=40, default='the beautiful Marina Village Baja Room in San Diego')
    about_address = models.CharField(max_length=40, default='The Address is 1939 Quivira Way San Diego California 92109')
    about_day = models.CharField(max_length=20, default='Saturday')
    about_date = models.CharField(max_length=50, default='26 March 2020')
    about_time = models.CharField(max_length=30, default='5.30 PM')
    about_brief1 = models.TextField(default='Your groom brief')
    about_brief2 = models.TextField(default='Your bride brief')
    about_image2 = models.ImageField(upload_to='img/jj/', blank=True, null=True)
    countdown_background = models.ImageField(upload_to='img/jj/', blank=True, null=True)
    
    # section 4
    album_image1 = models.ImageField(upload_to='img/jj/', blank=True, null=True)
    album_image2 = models.ImageField(upload_to='img/jj/', blank=True, null=True)
    album_image3 = models.ImageField(upload_to='img/jj/', blank=True, null=True)
    album_image4 = models.ImageField(upload_to='img/jj/', blank=True, null=True)
    album_image5 = models.ImageField(upload_to='img/jj/', blank=True, null=True)
    
    # section 5
    rsvp_image = models.ImageField(upload_to='img/jj/', blank=True, null=True)
    inv_pdf = models.FileField(upload_to='file/jj/', blank=True, null=True)

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
        return reverse('jackjane_detail', kwargs={'site_url': self.site_url})