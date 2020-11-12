from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from rsvp.themes.models import Theme
from django.utils import timezone
from ckeditor.fields import RichTextField


class VictorKarla(models.Model):
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    site_url = models.SlugField(unique=True, default='Your wedding invitation url. e.g. reservasidulu.com/bride-groom')
    
    # section 1
    title = models.CharField(max_length=40, default='Your wedding title')
    img_logo = models.ImageField(upload_to='img/victor/', blank=False, help_text='Your logo goes here')
    bride_name = models.CharField(max_length=30, default='Your bride name')
    groom_name = models.CharField(max_length=30, default='Your groom name')
    hashtag = models.CharField(max_length=30, default='Your #hashtag here')
    
    # section 2
    invite_brief = models.TextField(default='Your summary brief')
    
    # section 3
    story_bg = models.ImageField(upload_to='img/victor/', blank=True, null=True)
    story_brief_mobile = models.TextField(default='Your summary brief')
    
    # section 4
    gallery_image_thumbnail = models.ImageField(upload_to='img/victor/', blank=True, null=True)
    gallery_image_thumbnail_mobile = models.ImageField(upload_to='img/victor/', blank=True, null=True)
    gallery_image1 = models.ImageField(upload_to='img/victor/', blank=True, null=True)
    gallery_image2 = models.ImageField(upload_to='img/victor/', blank=True, null=True)
    gallery_image3 = models.ImageField(upload_to='img/victor/', blank=True, null=True)
    gallery_image4 = models.ImageField(upload_to='img/victor/', blank=True, null=True)
    gallery_image5 = models.ImageField(upload_to='img/victor/', blank=True, null=True)
    gallery_image6 = models.ImageField(upload_to='img/victor/', blank=True, null=True)
    gallery_image7 = models.ImageField(upload_to='img/victor/', blank=True, null=True)
    gallery_image8 = models.ImageField(upload_to='img/victor/', blank=True, null=True)
    gallery_image9 = models.ImageField(upload_to='img/victor/', blank=True, null=True)
    
    # section 5
    va_place = models.CharField(max_length=40, default='Fufu Kawaguchiko')
    va_brief = models.TextField(default='Your convenience is one of our priorities, we have booked you a room at this following place: ')
    va_address = models.TextField(default=' 2211-1 Mizuguchi, Kawaguchi-Aza, Fuji-Kawaguchiko-Machi, Minamitsuru-Gun, Yamanashi, 401-0304, Japan.')
    va_note = models.CharField(max_length=100, default=' *Please mention Victor & Karla when you reserve the room.')
    vr_place = models.CharField(max_length=40, default='Oshino Hakkai')
    vr_address = models.TextField(default='Shibokusa, Oshino, Minamitsuru District, Yamanashi 401-0511, Japan.')
    vr_date = models.CharField(max_length=50, default='Saturday, January 21st 2020.')
    vr_time = models.CharField(max_length=50, default='17:30 – Finish')
    vr_dress = models.CharField(max_length=50, default='Evening Gown/ Kimono')
    vr_note = models.CharField(max_length=100, default=' *We will be providing a shuttle bus for all of our guests from the resort to the venue.')
    vc_place = models.CharField(max_length=40, default='Hanano Cathedral')
    vc_address = models.TextField(default='Shibokusa, Oshino, Minamitsuru District, Yamanashi 401-0511, Japan.')
    vc_date = models.CharField(max_length=50, default='Friday, January 20th 2020.')
    vc_time = models.CharField(max_length=50, default='10:00 – 12:00PM')
    vc_dress = models.CharField(max_length=50, default='Formal Wear')
    vc_note = models.CharField(max_length=100, default=' *We will be providing a shuttle bus for all of our guests from the resort to the venue.')
    
    # section 6
    inv_pdf = models.FileField(upload_to='file/victor/', blank=True, null=True)    

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
        return reverse('victor_detail', kwargs={'site_url': self.site_url})

