from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from rsvp.themes.models import Theme
from django.utils import timezone
from ckeditor.fields import RichTextField


class VickyWanda(models.Model):
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    site_url = models.SlugField(unique=True, default='Your wedding invitation url. e.g. reservasidulu.com/bride-groom')
    
    #section 1
    title = models.CharField(max_length=40, default='Your wedding title')
    img_logogram = models.ImageField(upload_to='img/vicky/', blank=False, help_text='Your logo goes here')
    img_logotype = models.ImageField(upload_to='img/vicky/', blank=False, help_text='Your logo goes here')
    img_logotype_mobile = models.ImageField(upload_to='img/vicky/', blank=False, help_text='Your logo goes here')
    bride_name = models.CharField(max_length=30, default='Your bride name')
    groom_name = models.CharField(max_length=30, default='Your groom name')
    hashtag = models.CharField(max_length=30, default='Your #hashtag here')
	
    #section 2
    banner_title = models.CharField(max_length=50, default='Tying the knot with my favorite person')
    banner_bg = models.ImageField(upload_to='img/vicky/', blank=True, null=True)
	
    #section 3
    about_os_image = models.ImageField(upload_to='img/vicky/', blank=True, null=True)
    about_os_brief = models.TextField(default='Your story brief')
    about_gr_image = models.ImageField(upload_to='img/vicky/', blank=True, null=True)
    about_gr_brief = models.TextField(default='Your groom brief')
    about_br_image = models.ImageField(upload_to='img/vicky/', blank=True, null=True)
    about_br_brief = models.TextField(default='Your bride brief')
	
    #section 4
    vc_month = models.CharField(max_length=20, default='SEPTEMBER')
    vc_date = models.CharField(max_length=2, default='23')
    vc_year = models.CharField(max_length=4, default='2020')
    vc_place = models.CharField(max_length=40, default='Grand Mosque')
    vc_address = models.CharField(max_length=50, default='Manohara Street, B - 2, Milan, Italy')
    vc_image = models.ImageField(upload_to='img/vicky/', blank=True, null=True)
    vc_maps_link = models.CharField(max_length=50, default='Your maps link')
    vr_month = models.CharField(max_length=20, default='SEPTEMBER')
    vr_date = models.CharField(max_length=2, default='24')
    vr_year = models.CharField(max_length=4, default='2020')
    vr_place = models.CharField(max_length=40, default='Hotel Mulia Bali')
    vr_address = models.CharField(max_length=50, default='Seminyak, B - 2, Bali, Indonesia')
    vr_dress = models.CharField(max_length=50, default='Tropical Vibe Formal Dress, Suit ')
    vr_image = models.ImageField(upload_to='img/vicky/', blank=True, null=True)
    vr_maps_link = models.CharField(max_length=50, default='Your maps link')
	
    #section 5
    acm_image = models.ImageField(upload_to='img/vicky/', blank=True, null=True)
    acm_image_mobile = models.ImageField(upload_to='img/vicky/', blank=True, null=True)
    acm_place = models.CharField(max_length=40, default='HOTEL MULIA BALI')
    acm_subtitle = models.CharField(max_length=40, default='1 NIGHT, 1 BREAKFAST TREAT')
    acm_brief = models.TextField(default='Your summary brief')
    acm_note = models.CharField(max_length=100, default='*Please mention vicky & wanda, when you reserve them')
    acm_maps_link = models.CharField(max_length=50, default='Your maps link')
	
    #section 6
    gallery_image1 = models.ImageField(upload_to='img/vicky/', blank=True, null=True)
    gallery_image2 = models.ImageField(upload_to='img/vicky/', blank=True, null=True)
    gallery_image3 = models.ImageField(upload_to='img/vicky/', blank=True, null=True)
    gallery_image4 = models.ImageField(upload_to='img/vicky/', blank=True, null=True)
    gallery_image5 = models.ImageField(upload_to='img/vicky/', blank=True, null=True)
    gallery_image6 = models.ImageField(upload_to='img/vicky/', blank=True, null=True)
	
    #section 7
    rsvp_image = models.ImageField(upload_to='img/vicky/', blank=True, null=True)
    inv_pdf = models.FileField(upload_to='file/vicky/', blank=True, null=True)

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
        return reverse('vw_detail', kwargs={'site_url': self.site_url})
