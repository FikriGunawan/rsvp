from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from rsvp.themes.models import Theme
from django.utils import timezone
from ckeditor.fields import RichTextField


class PeterMary(models.Model):
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    site_url = models.SlugField(unique=True,
                                default='Your wedding invitation url. e.g. reservasidulu.com/bride-groom')

    # # section 1
    title = models.CharField(max_length=40, help_text='Your wedding title')
    # bride_name = models.CharField(max_length=30, default='Your bride name')
    # grome_name = models.CharField(max_length=30, default='Your gome name')
    # hashtag = models.CharField(max_length=30, default='Your ##hashtag here')
    # img_logo = models.ImageField(upload_to='img/against/', blank=False, help_text='Your logo goes here')
    # img_background1 = models.ImageField(upload_to='img/against/', blank=True)
    # img_background2 = models.ImageField(upload_to='img/against/', blank=True)
    # img_background3 = models.ImageField(upload_to='img/against/', blank=True)
    #
    # # section 2
    # about_quote = models.CharField(max_length=100, default='Your quote here')
    # about_quote_by = models.CharField(max_length=100, default='Quote by')
    # about_img1 = models.ImageField(upload_to='img/against/', blank=True, null=True, help_text='Your summary image')
    # about_img2 = models.ImageField(upload_to='img/against/', blank=True, null=True, help_text='Your summary image')
    # about_title = models.CharField(blank=False, max_length=200, help_text='Your summary brief title')
    # about = models.TextField(blank=False, help_text='Your summary brief')
    #
    # # section 3
    # ceremony_img = models.ImageField(upload_to='img/against/', blank=True, null=True)
    # ceremony_time = models.CharField(max_length=40, default='3:00pm – 4:00pm', help_text='Your cermony date time')
    # ceremony_location = RichTextField()
    #
    # reception_img = models.ImageField(upload_to='img/against/', blank=True, null=True)
    # reception_time = models.CharField(max_length=40, default='6:00pm – 7:00pm', help_text='Your cermony date time')
    # reception_location = RichTextField()
    #
    # # section 4
    # gallery1 = models.ImageField(blank=True, upload_to='img/against/', help_text='Your gallery')
    # gallery2 = models.ImageField(blank=True, upload_to='img/against/', help_text='Your gallery')
    # gallery3 = models.ImageField(blank=True, upload_to='img/against/', help_text='Your gallery')
    # gallery4 = models.ImageField(blank=True, upload_to='img/against/', help_text='Your gallery')
    #
    # rsvp_img = models.ImageField(upload_to='img/against/', null=True)
    #
    # created = models.DateTimeField(auto_now_add=True, auto_created=True, editable=False)
    # updated = models.DateTimeField(auto_created=True, auto_now=True, editable=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance = None

    def publish(self):
        self.published_date = timezone.now()

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('peter_detail', kwargs={'site_url': self.site_url})
