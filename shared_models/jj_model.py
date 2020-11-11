from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from rsvp.themes.models import Theme
from django.utils import timezone
from ckeditor.fields import RichTextField


class JackJane(models.Model):
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    site_url = models.SlugField(unique=True,
                                default='Your wedding invitation url. e.g. reservasidulu.com/undangan-mantan')

    # # section 1
    title = models.CharField(max_length=40, help_text='Your wedding title')
    bride_name = models.CharField(max_length=30, default='Your bride name')

    img_logo = models.ImageField(
        upload_to='img/jj/',
        blank=False,
        default='dp.png',
        help_text='Your logo goes here'
    )
    banner_bg1 = models.ImageField(upload_to='img/jj/', blank=True)
    banner_bg2 = models.ImageField(upload_to='img/jj/', blank=True)
    banner_bg3 = models.ImageField(upload_to='img/jj/', blank=True)

    # section 2
    section1_date = models.CharField(max_length=100, default='27/05/20')
    about_image1 = models.ImageField(upload_to='img/jj/', blank=True, null=True, help_text='Your image')
    about2_text = models.TextField(help_text='Your wedding place and address', default='')
    about2_time = models.CharField(max_length=100, help_text='Your date and time', default='')

    # section 3
    about3_name1 = models.CharField(blank=False, max_length=200, default='Men\'s name')
    about3_text1 = models.TextField(blank=False, default='Men summary')
    about3_name2 = models.CharField(blank=False, max_length=200, default='Woman\'s name')
    about3_text2 = models.TextField(blank=False, default='Woman summary')
    about3_image = models.ImageField(upload_to='img/jj/', blank=True, null=True, default='Your summary image')

    # section 4
    section4_background = models.ImageField(upload_to='img/jj/', blank=True, null=True)
    section4_time = models.DateTimeField(blank=True, null=True)

    # section 5
    album1 = models.ImageField(upload_to='img/jj/', blank=True, null=True, help_text='Your album')
    album2 = models.ImageField(upload_to='img/jj/', blank=True, null=True, help_text='Your album')
    album3 = models.ImageField(upload_to='img/jj/', blank=True, null=True, help_text='Your album')
    album4 = models.ImageField(upload_to='img/jj/', blank=True, null=True, help_text='Your album')
    album5 = models.ImageField(upload_to='img/jj/', blank=True, null=True, help_text='Your album')

    # last section
    rsvp_image = models.ImageField(upload_to='img/jj/', blank=True, null=True, help_text='Your RSVP Image')
    inv_pdf = models.FileField(upload_to='jj/', blank=True, null=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance = None

    def publish(self):
        self.published_date = timezone.now()

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('jackjane_detail', kwargs={'site_url': self.site_url})
