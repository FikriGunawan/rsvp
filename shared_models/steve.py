from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from rsvp.themes.models import Theme
from django.utils import timezone
from ckeditor.fields import RichTextField


class SteveSharon(models.Model):
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    site_url = models.SlugField(unique=True, default='Your wedding invitation url. e.g. reservasidulu.com/bride-groom')

    # section 1
    title = models.CharField(max_length=40, default='Your wedding title')
    img_logo = models.ImageField(upload_to='img/steve/', blank=False, help_text='Your logo goes here')
    bride_name = models.CharField(max_length=30, default='Your bride name')
    groom_name = models.CharField(max_length=30, default='Your groom name')
    hashtag = models.CharField(max_length=30, default='Your #hashtag here')

	# section 2
    banner_title = models.CharField(max_length=50, default='Through Thick and Thin')
    banner_bg = models.ImageField(upload_to='img/steve/', blank=True, null=True)
	
    # section 3
    story_image = models.ImageField(upload_to='img/steve/', blank=True, null=True)
    story_brief = models.TextField(default='Your summary brief')
    story_gr_name = models.CharField(max_length=30, default='STEVE ROBERTS')
    story_gr_brief = models.TextField(default='Your groom brief')
    story_br_name = models.CharField(max_length=30, default='SHARON CARTIER')
    story_br_brief = models.TextField(default='Your bride brief')
	
    # section 4
    vc_title = models.CharField(max_length=40, default='OUR WEDDING CEREMONY')
    vc_maps_link = models.CharField(max_length=50, default='Your maps link')
    vc_date = models.CharField(max_length=2, default='23')
    vc_my = models.CharField(max_length=30, default='September 2020')
    vc_time = models.CharField(max_length=50, default='10:00 am till 12:00 pm')
    vc_place = models.CharField(max_length=50, default='Grand Chapel of Toronto, Canada')
    vc_address = models.CharField(max_length=50, default='Holy Spirit Street, 3-5 A, Glass Boulevard, Water Village')
    vc_image = models.ImageField(upload_to='img/steve/', blank=True, null=True)
    vr_title = models.CharField(max_length=40, default='OUR WEDDING GARDEN PARTY')
    vr_maps_link = models.CharField(max_length=50, default='Your maps link')
    vr_date = models.CharField(max_length=2, default='24')
    vr_my = models.CharField(max_length=30, default='September 2020')
    vr_time = models.CharField(max_length=50, default='05:00 pm till 07:00 pm')
    vr_place = models.CharField(max_length=50, default='Flower Palace Toronto, Canada')
    vr_address = models.CharField(max_length=50, default='Legendary Street, 14 B, Southern Sea, Ocean Hill')
    vr_dress = models.CharField(max_length=50, default='Simple Minimal Formal Attire, No Complicated Sequence, Plain Sophisticated look')
    vr_image = models.ImageField(upload_to='img/steve/', blank=True, null=True)
	
    # section 5
    acm_image = models.ImageField(upload_to='img/steve/', blank=True, null=True)
    acm_place = models.CharField(max_length=40, default='THE CONFIDANTE')
    acm_subtitle = models.CharField(max_length=40, default='1 Night Stay | 1 Suite Bedroom')
    acm_brief = models.TextField(default='Your summary brief')
    acm_maps_link = models.CharField(max_length=50, default='Your maps link')
	
    # section 6
    gallery_brief = models.TextField(default='Your summary brief')
    gallery_image1 = models.ImageField(upload_to='img/steve/', blank=True, null=True)
    gallery_image2 = models.ImageField(upload_to='img/steve/', blank=True, null=True)
    gallery_image3 = models.ImageField(upload_to='img/steve/', blank=True, null=True)
    gallery_image4 = models.ImageField(upload_to='img/steve/', blank=True, null=True)
    gallery_image5 = models.ImageField(upload_to='img/steve/', blank=True, null=True)
    gallery_image6 = models.ImageField(upload_to='img/steve/', blank=True, null=True)
	
    # section 7
    inv_pdf = models.FileField(upload_to='file/steve/', blank=True, null=True)

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
        return reverse('steve_detail', kwargs={'site_url': self.site_url})
