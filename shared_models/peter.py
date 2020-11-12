from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from rsvp.themes.models import Theme
from django.utils import timezone
from ckeditor.fields import RichTextField


class PeterMary(models.Model):
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    site_url = models.SlugField(unique=True,
                                default='Your wedding invitation url. e.g. reservasidulu.com/bride-groom')
    # section 1
       title = models.CharField(max_length=40, default='Your wedding title')
       img_logo = models.ImageField(upload_to='img/peter/', blank=False, help_text='Your logo goes here')
       bride_name = models.CharField(max_length=30, default='Your bride name')
       groom_name = models.CharField(max_length=30, default='Your groom name')
       hashtag = models.CharField(max_length=30, default='Your #hashtag here')
    # section 2
       banner_bg = models.ImageField(upload_to='img/peter/', blank=True, null=True)
       banner_bg_mobile = models.ImageField(upload_to='img/peter/', blank=True, null=True)
    # section 3
       about_title1 = models.CharField(max_length=50, default='Title')
       about_brief1 = models.TextField(default='Your summary brief')
       about_image_text1 = models.ImageField(upload_to='img/peter/', blank=True, null=True)
       about_image1 = models.ImageField(upload_to='img/peter/', blank=True, null=True)
       about_image1_mobile = models.ImageField(upload_to='img/peter/', blank=True, null=True)
       about_image2 = models.ImageField(upload_to='img/peter/', blank=True, null=True)
       about_title2 = models.CharField(max_length=30, default='Title')
       about_brief2 = models.TextField(default='Your summary brief')
       about_image3 = models.ImageField(upload_to='img/peter/', blank=True, null=True)
       about_image3_mobile = models.ImageField(upload_to='img/peter/', blank=True, null=True)
       about_title3 = models.CharField(max_length=30, default='Title')
       about_brief3 = models.TextField(default='Your summary brief')
    # section 4
       venue_image = models.ImageField(upload_to='img/peter/', blank=True, null=True)
       vc_date = models.CharField(max_length=30, default='Date')
       vc_place = models.CharField(max_length=30, default='Place')
       vc_address = models.TextField(default='Your summary brief') 
       vc_time = models.CharField(max_length=30, default='Time')
       vr_date = models.CharField(max_length=30, default='Date')
       vr_place = models.CharField(max_length=30, default='Place')
       vr_address = models.TextField(default='Your summary brief')
       vr_time = models.CharField(max_length=30, default='Time')
       vr_dress = models.CharField(max_length=30, default='Dresscode')
    # section 5
       gallery_brief = models.ImageField(upload_to='img/peter/', blank=True, null=True)
       gallery_image1 = models.ImageField(upload_to='img/peter/', blank=True, null=True)
       gallery_image2 = models.ImageField(upload_to='img/peter/', blank=True, null=True)
       gallery_image3 = models.ImageField(upload_to='img/peter/', blank=True, null=True)
       gallery_image4 = models.ImageField(upload_to='img/peter/', blank=True, null=True)
       gallery_image5 = models.ImageField(upload_to='img/peter/', blank=True, null=True)
       gallery_image6 = models.ImageField(upload_to='img/peter/', blank=True, null=True)
       gallery_image7 = models.ImageField(upload_to='img/peter/', blank=True, null=True)
       gallery_image8 = models.ImageField(upload_to='img/peter/', blank=True, null=True)
    # section 6
       acm_image = models.ImageField(upload_to='img/peter/', blank=True, null=True)
       acm_place = models.ImageField(upload_to='img/peter/', blank=True, null=True)
       acm_brief = models.TextField(default='Your summary brief')
       acm_maps_link =  models.CharField(max_length=30, default='Date')
    # section 7
       inv_pdf = models.FileField(upload_to='file/lucas/', blank=True, null=True)

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
        return reverse('peter_detail', kwargs={'site_url': self.site_url})
