from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from rsvp.themes.models import Theme
from django.utils import timezone


class DianaRoss(models.Model):
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    site_url = models.SlugField(unique=True,
                                help_text='Your birthday invitation url. e.g. reservasidulu.com/polka-galore')

    # section 1
        title =  models.CharField(max_length=40, default='Birthday title')
        about_name = models.CharField(max_length=40, default='Name')
    # section 2
        banner_logo = models.ImageField(upload_to='img/diana_ross/', blank=True, null=True)
        banner_logo_mobile = models.ImageField(upload_to='img/diana_ross/', blank=True, null=True)
    # section 3
        about_brief = models.TextField(default='Brief')
        about_image = models.ImageField(upload_to='img/diana_ross/', blank=True, null=True)
    # section 4
        dap_brief = models.TextField(default='Brief')
        dap_date = models.CharField(max_length=40, default='Date')
        dap_month = models.CharField(max_length=40, default='Month')
        dap_year = models.CharField(max_length=40, default='Year')
        dap_time = models.CharField(max_length=40, default='Time')
        dap_place = models.CharField(max_length=40, default='Place')
        dap_room = models.CharField(max_length=40, default='Room')
        dap_maps = models.CharField(max_length=40, default='Maps Link')
        dap_place_image = models.ImageField(upload_to='img/diana_ross/', blank=True, null=True)
        dap_desc = models.TextField(default='Desc')
        dap_dress = models.CharField(max_length=40, default='Dress')
        dap_desc_image = models.ImageField(upload_to='img/diana_ross/', blank=True, null=True)
    # section 5
        gallery_image1 = models.ImageField(upload_to='img/diana_ross/', blank=True, null=True)
        gallery_image2 = models.ImageField(upload_to='img/diana_ross/', blank=True, null=True)
        gallery_image3 = models.ImageField(upload_to='img/diana_ross/', blank=True, null=True)
        gallery_image4 = models.ImageField(upload_to='img/diana_ross/', blank=True, null=True)
        gallery_image5 = models.ImageField(upload_to='img/diana_ross/', blank=True, null=True)
        gallery_image6 = models.ImageField(upload_to='img/diana_ross/', blank=True, null=True)
        gallery_image7 = models.ImageField(upload_to='img/diana_ross/', blank=True, null=True)
        gallery_image8 = models.ImageField(upload_to='img/diana_ross/', blank=True, null=True)
        gallery_image9 = models.ImageField(upload_to='img/diana_ross/', blank=True, null=True)
    # section 6
        inv_pdf = models.FileField(upload_to='file/diana_ross/', blank=True, null=True)

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
        return reverse('diana_ross_detail', kwargs={'site_url': self.site_url})

