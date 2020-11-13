from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from rsvp.themes.models import Theme
from django.utils import timezone
from ckeditor.fields import RichTextField


class DylanRose(models.Model):
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    site_url = models.SlugField(unique=True, default='Your wedding invitation url. e.g. reservasidulu.com/bride-groom')

    # section 1
    title = models.CharField(max_length=40, default='Your wedding title')
    img_logo = models.ImageField(upload_to='img/dylan/', blank=True, help_text='Your logo goes here')
    bride_name = models.CharField(max_length=30, default='Your bride name')
    groom_name = models.CharField(max_length=30, default='Your groom name')
    hashtag = models.CharField(max_length=30, default='Your #hashtag here')

	# section 2
    banner_bg = models.ImageField(upload_to='img/dylan/', blank=True, null=True)
    banner_bg_mobile = models.ImageField(upload_to='img/dylan/', blank=True, null=True)

	# section 3
    story_image = models.ImageField(upload_to='img/dylan/', blank=True, null=True)
    story_brief = models.TextField(default='Your summary brief')

	# section 4
    vc_day = models.CharField(max_length=20, default='Saturday')
    vc_date = models.CharField(max_length=50, default='22th July 2020')
    vc_time = models.CharField(max_length=30, default='11.00 am')
    vc_address = models.TextField(default='Jl. Pantai Suluban, Pecatu, Kuta Sel., Kabupaten Badung, Uluwatu, Bali, Indonesia')
    vc_dress = models.CharField(max_length=30, default='Casual Elegant')
    vc_image = models.ImageField(upload_to='img/dylan/', blank=True, null=True)
    vr_day = models.CharField(max_length=20, default='Saturday')
    vr_date = models.CharField(max_length=50, default='22th July 2020')
    vr_time = models.CharField(max_length=30, default='05.00 pm')
    vr_address = models.TextField(default='Jl. Pantai Kolang Kaling, Seminyak, Kuta Sel. Kabupaten Badung, Bali, Indonesia')
    vr_dress = models.CharField(max_length=30, default='Formal')
    vr_image = models.ImageField(upload_to='img/dylan/', blank=True, null=True)

	# section 5
    acm_image = models.ImageField(upload_to='img/dylan/', blank=True, null=True)
    acm_place = models.CharField(max_length=50, default='The Wyatt Hotel')
    acm_address = models.TextField(default='Kuta, Bali, Indonesia (212) 555-0123')
    acm_note = models.CharField(max_length=100, default=' *Please mention Dylan & Rose wedding when you reserve the room* ')

	# section 6
    memories_brief = models.TextField(default='These memories are captured with passion and love by the one and only Memoir Photography ')
    memories_image1 = models.ImageField(upload_to='img/dylan/', blank=True, null=True)
    memories_image2 = models.ImageField(upload_to='img/dylan/', blank=True, null=True)
    memories_image3 = models.ImageField(upload_to='img/dylan/', blank=True, null=True)
    memories_image4 = models.ImageField(upload_to='img/dylan/', blank=True, null=True)
    
	# section 7
    inv_pdf = models.FileField(upload_to='file/dylan/', blank=True, null=True)

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
        return reverse('dylan_detail', kwargs={'site_url': self.site_url})