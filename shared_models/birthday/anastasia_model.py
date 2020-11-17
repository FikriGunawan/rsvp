from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from rsvp.themes.models import Theme


class Anastasia(models.Model):
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)

    site_url = models.SlugField()
    title = models.CharField(max_length=40, help_text='Your birthday title')
    subtitle = models.CharField(max_length=40, help_text='Your birthday subtitle')
    img_background = models.ImageField(upload_to='img/anastasia/', blank=True)

    date = models.DateField()
    day = models.CharField(default='Sunday', max_length=8, help_text='Your birth-day')
    hour = models.TimeField()

    place = models.CharField(max_length=100, help_text='Your birthday place')
    dresscode = models.CharField(max_length=20, help_text='Your birthday dresscode')

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
        return reverse('anastasia_detail', kwargs={'site_url': self.site_url})
