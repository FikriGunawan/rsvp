from django.db import models
from django.contrib.auth.models import User
from rsvp.themes.models import Theme
from django.utils import timezone
from ckeditor.fields import RichTextField


class NatashaBruce(models.Model):
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    site_url = models.SlugField(unique=True,
                                help_text='Your wedding invitation url. e.g. reservasidulu.com/undangan-mantan')

    # section 1
    title = models.CharField(max_length=40, help_text='Your wedding title')
    # background_img = models.ImageField(upload_to='img/natasha_bruce/', blank=False)
    #
    # story_img1 = models.ImageField(upload_to='img/natasha_bruce/', blank=False)
    # story_img2 = models.ImageField(upload_to='img/natasha_bruce/', blank=False)
    # story_text = RichTextField()
    #
    # groom_img1 = models.ImageField(upload_to='img/natasha_bruce/', blank=False)
    # groom_img2 = models.ImageField(upload_to='img/natasha_bruce/', blank=False)
    #
    # groom_men = models.CharField(max_length=50, help_text='Your groom name (Name)')
    # groom_woman = models.CharField(max_length=50, help_text='Your groom name (Woman)')
    #
    # groom_brief1 = models.TextField(blank=False)
    # groom_brief2 = models.TextField(blank=False)
    #
    # location1 = RichTextField()
    # location2 = RichTextField()
    #
    # location1_img = models.ImageField(upload_to='img/natasha_bruce', blank=False)
    # location2_img = models.ImageField(upload_to='img/natasha_bruce', blank=False)
    #
    # # accommodation
    # hotel_name = models.CharField(max_length=30, help_text='Your hotel accommodation')
    # hotel_img = models.ImageField(upload_to='img/natasha_bruce/', blank=True)
    # hotel_brief = RichTextField()
    # hotel_location = models.CharField(max_length=200)
    #
    # gallery1 = models.ImageField(blank=True, upload_to='img/natasha_bruce/', help_text='Your gallery')
    # gallery2 = models.ImageField(blank=True, upload_to='img/natasha_bruce/', help_text='Your gallery')
    # gallery3 = models.ImageField(blank=True, upload_to='img/natasha_bruce/', help_text='Your gallery')
    # gallery4 = models.ImageField(blank=True, upload_to='img/natasha_bruce/', help_text='Your gallery')
    #
    # date = models.DateField(blank=False)
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
        return reverse('alive_detail', kwargs={'site_url': self.site_url})
