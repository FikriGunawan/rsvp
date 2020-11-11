from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from rsvp.themes.models import Theme
from django.utils import timezone
from ckeditor.fields import RichTextField


class Lucas(models.Model):
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    site_url = models.SlugField(unique=True, default='Your wedding invitation url. e.g. reservasidulu.com/bride-groom')

    # section 1    
    title = models.CharField(max_length=40, default='Your wedding title')
    bride_name = models.CharField(max_length=30, default='Your bride name')
    groom_name = models.CharField(max_length=30, default='Your groom name')
    hashtag = models.CharField(max_length=30, default='Your #hashtag here')
    
    # section 2
    banner_date = models.CharField(max_length=40, default='OCTOBER 18TH 2020')
    banner_title = models.CharField(max_length=50, default='Lucas & Eliza')
    banner_bg = models.ImageField(upload_to='img/lucas/', blank=True, null=True)
    banner_bg_mobile = models.ImageField(upload_to='img/lucas/', blank=True, null=True)

    # section 3
    story_brief = models.TextField(default='Your summary brief')
    story_meet =  models.CharField(max_length=50, default='the boat in Manila, Malaysia')
    story_date_at =  models.CharField(max_length=50, default='2012, at Malaysia Bird’s Zoo')
    story_know_each_other =  models.CharField(max_length=40, default='5 years')
    story_pet =  models.CharField(max_length=40, default='called Nemo')
    story_hobby =  models.CharField(max_length=40, default='to cook')
    story_engaged =  models.CharField(max_length=4, default='2019')
    
    # section 4
    gallery_image1 = models.ImageField(upload_to='img/lucas/', blank=True, null=True)
    gallery_image2 = models.ImageField(upload_to='img/lucas/', blank=True, null=True)
    gallery_image3 = models.ImageField(upload_to='img/lucas/', blank=True, null=True)
    gallery_image4 = models.ImageField(upload_to='img/lucas/', blank=True, null=True)
    gallery_image5 = models.ImageField(upload_to='img/lucas/', blank=True, null=True)
    gallery_image6 = models.ImageField(upload_to='img/lucas/', blank=True, null=True)
    gallery_image7 = models.ImageField(upload_to='img/lucas/', blank=True, null=True)
    gallery_image8 = models.ImageField(upload_to='img/lucas/', blank=True, null=True)
    gallery_image9 = models.ImageField(upload_to='img/lucas/', blank=True, null=True)
    
    # section 5
    vmaps_image = models.ImageField(upload_to='img/lucas/', blank=True, null=True)
    vc_image = models.ImageField(upload_to='img/lucas/', blank=True, null=True)
    vc_date = models.CharField(max_length=50, default='20 November 2020')
    vc_day = models.CharField(max_length=20, default='Saturday')
    vc_time = models.CharField(max_length=30, default='10AM to 12PM')
    vc_loc = models.CharField(max_length=50, default='La Brea Community Church')
    vc_dress = models.CharField(max_length=30, default='Formal Wear')
    vc_parking = models.CharField(max_length=30, default='Free Valet on Site')
    vr_image = models.ImageField(upload_to='img/lucas/', blank=True, null=True)
    vr_date = models.CharField(max_length=50, default='21 November 2020')
    vr_day = models.CharField(max_length=20, default='Sunday')
    vr_time = models.CharField(max_length=30, default='6PM to Finish')
    vr_loc = models.CharField(max_length=50, default='Palladio Banquet Hall')
    vr_dress = models.CharField(max_length=30, default='Evening Wear')
    vr_parking = models.CharField(max_length=30, default='Free Valet on Site')
    
    # section 6
    acm_image = models.ImageField(upload_to='img/lucas/', blank=True, null=True)
    acm_place = models.CharField(max_length=100, default='Palihotel')
    acm_address = models.CharField(max_length=100, default='7950 Melrose Ave, Los Angeles, CA 90046.')
    acm_note = models.TextField(default='Your convenience is one of our priorities, we have booked you a room. Please mention Lucas & Eliza when you reserve the room. ')
    
    # section 7
    rsvp_popup_img = models.ImageField(upload_to='img/lucas/', blank=True, null=True)
    rsvp_popup_name = models.CharField(max_length=100, default='Wanda')
    rsvp_popup_phone = models.CharField(max_length=100, default='099-800-9999')
    inv_pdf = models.FileField(upload_to='file/lucas/', blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True, auto_created=True, editable=False)
    updated = models.DateTimeField(auto_created=True, auto_now=True, editable=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance = None

    def publish(self):
        self.published_date = timezone.now()

    def __str__(self):
        return str(self.bride_name)

    def get_absolute_url(self):
        return reverse('alive_detail', kwargs={'site_url': self.site_url})
