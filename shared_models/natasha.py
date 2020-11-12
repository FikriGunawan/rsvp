from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from rsvp.themes.models import Theme
from django.utils import timezone
from ckeditor.fields import RichTextField


class NatashaBruce(models.Model):
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    site_url = models.SlugField(unique=True,
                                help_text='Your wedding invitation url. e.g. reservasidulu.com/bushes-and-leaves')
    # section 1
    title = models.CharField(max_length=40, help_text='Your wedding title')
    img_logo = models.ImageField(upload_to='img/natasha/', blank=False, help_text='Your logo goes here')
    bride_name = models.CharField(max_length=30, default='Your bride name')
    groom_name = models.CharField(max_length=30, default='Your groom name')
    hashtag = models.CharField(max_length=30, default='Your #hashtag here')

    # section 2
    banner_bg = models.ImageField(upload_to='img/natasha/', blank=True)
    banner_bg_mobile = models.ImageField(upload_to='img/natasha/', blank=True)
    story_image1 = models.ImageField(upload_to='img/natasha/', blank=True, null=True, help_text='Your summary image')
    story_image2 = models.ImageField(upload_to='img/natasha/', blank=True, null=True, help_text='Your summary image')
    story_desc = models.TextField(blank=False, default='Your summary brief')
    # section 3
    about_gr_name = models.CharField(max_length=30, default='Your groom name')
    about_gr_brief = models.TextField(blank=False, default='Your summary brief')
    about_gr_image = models.ImageField(upload_to='img/natasha/', blank=True, null=True, help_text='Your summary image')
    about_gr_image_mobile = models.ImageField(upload_to='img/natasha/', blank=True, null=True, help_text='Your summary image')
    about_br_name = models.CharField(max_length=30, default='Your bride name')
    about_br_brief = models.TextField(blank=False, default='Your summary brief')
    about_br_image = models.ImageField(upload_to='img/natasha/', blank=True, null=True, help_text='Your summary image')
    about_br_image_mobile = models.ImageField(upload_to='img/natasha/', blank=True, null=True, help_text='Your summary image')
    # section 4
    vc_image = models.ImageField(upload_to='img/natasha/', blank=True, null=True, help_text='Your summary image')
    vc_place = models.CharField(max_length=30, default='Your place')
    vc_day = models.CharField(max_length=30, default='Day')
    vc_date = models.CharField(max_length=30, default='Date')
    vc_time = models.CharField(max_length=30, default='Time')
    vc_address = models.TextField(blank=False, default='Address')
    vc_dress = models.CharField(max_length=30, default='Dresscode')
    vc_maps_link = models.CharField(max_length=30, default='Map Links')
    vr_image = models.ImageField(upload_to='img/natasha/', blank=True, null=True, help_text='Your summary image')
    vr_place = models.CharField(max_length=30, default='Your place')
    vr_day = models.CharField(max_length=30, default='Day')
    vr_date = models.CharField(max_length=30, default='Date')
    vr_time = models.CharField(max_length=30, default='Time')
    vr_address = models.TextField(blank=False, default='Address')
    vr_dress = models.CharField(max_length=30, default='Dresscode')
    vr_maps_link = models.CharField(max_length=30, default='Map Links')
    # section 5
    acm_image = models.ImageField(upload_to='img/natasha/', blank=True, null=True, help_text='Your summary image')
    acm_place = models.CharField(max_length=30, default='Your place')
    acm_subtitle = models.CharField(max_length=30, default='Subtitle')
    acm_brief = models.CharField(max_length=30, default='Your place')
    acm_maps_link = models.CharField(max_length=30, default='Map Links')
    # section 6
    gallery_image1 = models.ImageField(upload_to='img/natasha/', blank=True, null=True, help_text='Your summary image')
    gallery_image2 = models.ImageField(upload_to='img/natasha/', blank=True, null=True, help_text='Your summary image')
    gallery_image3 = models.ImageField(upload_to='img/natasha/', blank=True, null=True, help_text='Your summary image')
    gallery_image4 = models.ImageField(upload_to='img/natasha/', blank=True, null=True, help_text='Your summary image')
    # section 7
    inv_pdf = models.FileField(upload_to='file/natasha/', blank=True, null=True)

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
        return reverse('natasha_detail', kwargs={'site_url': self.site_url})
