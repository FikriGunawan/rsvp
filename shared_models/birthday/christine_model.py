from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from rsvp.themes.models import Theme
from django.utils import timezone
from ckeditor.fields import RichTextField


class Christine(models.Model):
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    site_url = models.SlugField(unique=True, default='Your wedding invitation url. e.g. reservasidulu.com/fun-times')

    # section 1
        title = models.CharField(max_length=40, default='Birthday title')
        about_name =  models.CharField(max_length=40, default='Name')
        about_age =  models.CharField(max_length=40, default='Age of spade')
    # section 2
        banner_subtitle = models.CharField(max_length=40, default='Subtitle')
        banner_title = models.CharField(max_length=40, default='Banner title')
        banner_bg = models.ImageField(upload_to='img/christine/', blank=True, null=True)
        banner_bg_mobile =  models.ImageField(upload_to='img/christine/', blank=True, null=True)
    # section 3
        about_brief = models.TextField(default='Your summary brief')
        brief_image1 = models.ImageField(upload_to='img/christine/', blank=True, null=True)
        brief_image2 = models.ImageField(upload_to='img/christine/', blank=True, null=True)
        brief_image3 = models.ImageField(upload_to='img/christine/', blank=True, null=True)
        brief_desc = models.TextField(default='Your summary brief')
    # section 4
        dap_day = models.CharField(max_length=40, default='Day')
        dap_date = models.CharField(max_length=40, default='Date')
        dap_time = models.CharField(max_length=40, default='Time')
        dap_place = models.CharField(max_length=40, default='Place')
        dap_address = models.TextField(default='Address')
        dap_dress = models.CharField(max_length=40, default='Dress')
    # section 5
        inv_pdf = models.FileField(upload_to='file/chrsitine/', blank=True, null=True)

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
        return reverse('christine_detail', kwargs={'site_url': self.site_url})
