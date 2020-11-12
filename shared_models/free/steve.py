from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from rsvp.themes.models import Theme
from django.utils import timezone
from ckeditor.fields import RichTextField


class FreeSteveSharon(models.Model):
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    site_url = models.SlugField(unique=True, default='Your wedding invitation url. e.g. reservasidulu.com/free-blooming-feelings')

    # section 1
        title = models.CharField(max_length=40, default='Your wedding title')
        name_bride = models.CharField(max_length=30, default='Your bride name')
        name_groom = models.CharField(max_length=30, default='Your groom name')
        hashtag = models.CharField(max_length=30, default='Your #hashtag here')
	# section 2
        image = models.ImageField(upload_to='img/free/steve/', blank=True, null=True)
        vc_place = models.CharField(max_length=50, default='Grand Chapel of Toronto, Canada')
        vc_address = models.CharField(max_length=50, default='Holy Spirit Street, 3-5 A, Glass Boulevard, Water Village')
        vc_date = models.CharField(max_length=2, default='Date')
        vc_month = models.CharField(max_length=30, default='Month')
        vc_year = models.CharField(max_length=30, default='Year')
        vc_time = models.CharField(max_length=30, default='Time')
        vp_place = models.CharField(max_length=30, default='Place')
        vp_address = models.TextField(default='Your summary brief')
        vp_date = models.CharField(max_length=2, default='Date')
        vp_month = models.CharField(max_length=30, default='Month')
        vp_year = models.CharField(max_length=30, default='Year')
        vp_time = models.CharField(max_length=30, default='Time')

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
        return reverse('free_steve_detail', kwargs={'site_url': self.site_url})
