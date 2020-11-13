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
                                default='Your wedding invitation url. e.g. reservasidulu.com/passionate-bond')

    # section 1
        title = models.CharField(max_length=40, help_text='Your wedding title')
        initial_logo = models.ImageField(upload_to='img/liam/', blank=True, null=True, help_text='Your logo image')
        groom_name = models.CharField(max_length=30, default='Your groom name')
        bride_name = models.CharField(max_length=30, default='Your bride name')
        hashtag = models.CharField(max_length=30, default='Your #hashtag here')
    # section 2
        banner_title = models.CharField(max_length=40, default='Your title')
        banner_bg = models.ImageField(upload_to='img/liam/', blank=True, null=True, help_text='Your banner image')
        about_image = models.ImageField(upload_to='img/liam/', blank=True, null=True, help_text='About image')
        about_title = models.CharField(max_length=40, default='Your title')
        about_brief = models.TextField(blank=False, default='Your summary brief')
    # section 3
        vc_image = models.ImageField(upload_to='img/liam/', blank=True, null=True, help_text='Your image')
        vc_day = models.CharField(max_length=40, default='Saturday')
        vc_date = models.CharField(max_length=40, default='22th')
        vc_time = models.CharField(max_length=40, default='3:00pm – 4:00pm')
        vc_place = models.CharField(max_length=40, default='New Faith Church')
        vc_address = models.TextField(blank=False, default='Address detail')
        vr_image = models.ImageField(upload_to='img/liam/', blank=True, null=True, help_text='Your image')
        vr_day = models.CharField(max_length=40, default='Saturday')
        vr_date = models.CharField(max_length=40, default='22th')
        vr_time = models.CharField(max_length=40, default='3:00pm – 4:00pm')
        vr_place = models.CharField(max_length=40, default='New Faith Church')
        vr_address = models.TextField(blank=False, default='Address detail')
    # section 4
        acm_image = models.ImageField(upload_to='img/liam/', blank=True, null=True, help_text='Your image')
        acm_place = models.CharField(max_length=40, default='Place')
        acm_address = models.TextField(blank=False, default='Address Detail')
        acm_note = models.TextField(blank=False, default='Note Detail')
    # section 5
        gallery_image1 = models.ImageField(upload_to='img/liam/', blank=True, null=True, help_text='Your image')
        gallery_image2 = models.ImageField(upload_to='img/liam/', blank=True, null=True, help_text='Your image')
        gallery_image3 = models.ImageField(upload_to='img/liam/', blank=True, null=True, help_text='Your image')
        gallery_image4 = models.ImageField(upload_to='img/liam/', blank=True, null=True, help_text='Your image')
        gallery_image5 = models.ImageField(upload_to='img/liam/', blank=True, null=True, help_text='Your image')
    # section 6
        inv_pdf = models.FileField(upload_to='file/liam/', blank=True, null=True)

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
