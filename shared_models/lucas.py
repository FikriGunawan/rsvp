from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from rsvp.themes.models import Theme
from django.utils import timezone
from ckeditor.fields import RichTextField


class Lucas(models.Model):
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)

    site_url = models.SlugField(unique=True,
                                default='Your wedding invitation url. e.g. reservasidulu.com/undangan-mantan')

    # section 1
    bride_name = models.CharField(max_length=30, default='Your bride name')
    grome_name = models.CharField(max_length=30, default='Your gome name')
    hashtag = models.CharField(max_length=30, default='Your #hastag here')

    # section 2
    banner_date = models.CharField(max_length=100, help_text='Your date here', blank=True, null=True)
    banner_title = models.CharField(max_length=100, default='Lucas & Eliza')
    banner_bg = models.ImageField(upload_to='img/lucas/', blank=True, null=True, help_text='banner desktop')
    banner_bg_mobile = models.ImageField(upload_to='img/lucas/', blank=True, null=True, help_text='banner mobile')

    # about_title = models.CharField(blank=False, max_length=200, help_text='Your summary brief title')
    # about = models.TextField(blank=False, help_text='Your summary brief')
    #
    # # section 3
    # ceremony_img = models.ImageField(upload_to='img/alive/', blank=True, null=True)
    # ceremony_time = models.CharField(max_length=40, default='3:00pm – 4:00pm', help_text='Your ceremony date time')
    # ceremony_location = RichTextField()
    #
    # reception_img = models.ImageField(upload_to='img/alive/', blank=True, null=True)
    # reception_time = models.CharField(max_length=40, default='6:00pm – 7:00pm', help_text='Your ceremony date time')
    # reception_location = RichTextField()
    #
    # # section 4
    # gallery1 = models.ImageField(blank=True, upload_to='img/alive/', help_text='Your gallery')
    # gallery2 = models.ImageField(blank=True, upload_to='img/alive/', help_text='Your gallery')
    # gallery3 = models.ImageField(blank=True, upload_to='img/alive/', help_text='Your gallery')
    # gallery4 = models.ImageField(blank=True, upload_to='img/alive/', help_text='Your gallery')

    rsvp_image = models.ImageField(upload_to='img/alive/', null=True, blank=True)
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
