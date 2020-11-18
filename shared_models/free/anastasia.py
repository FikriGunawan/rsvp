from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from rsvp.themes.models import Theme
from django.utils import timezone
from ckeditor.fields import RichTextField


class FreeAnastasia(models.Model):
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    site_url = models.SlugField(unique=True, default='Your birthday invitation url. e.g. reservasidulu.com/cindy-anastasia')

    # section 1
    title = models.CharField(max_length=40, help_text='Your birthday title')
    name = models.CharField(max_length=30, default='Your name')
    age = models.CharField(max_length=10, default='18th')
    hashtag = models.CharField(max_length=30, default='Your #hashtag here')

    # section 2
    image = models.ImageField(upload_to='img/free/anastasia/', blank=True, null=True)
    date = models.CharField(max_length=10, default='25.04.2020')
    day = models.CharField(max_length=10, default='SAT')
    time = models.CharField(max_length=20, default='5.30 PM')
    place = models.CharField(max_length=40, default='Marina Village Baja Room')
    address = models.CharField(max_length=50, default='939 Quivira Way, San Diego California 92109')
    dress = models.CharField(max_length=40, default='Black and White')

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
        return reverse('free_anastasia_detail', kwargs={'site_url': self.site_url})
