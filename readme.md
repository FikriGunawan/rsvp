https://reservasidulu.com models example

Model Reference Examples.

```python

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from rsvp.themes.models import Theme
from django.utils import timezone
from ckeditor.fields import RichTextField

class TemplateName(models.Model):
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    site_url = models.SlugField(unique=True, default='Your wedding invitation url. e.g. reservasidulu.com/bride-groom')


    Char 100 = models.CharField(max_length=100, default='Your title')
    Text < 255 = models.TextField(default='Your summary brief')
    Image upload = models.ImageField(upload_to='img/<theme_name>/', blank=True, null=True)
    File upload = models.FileField(upload_to='file/<theme_name>/', blank=True, null=True)
    

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
        return reverse('filename_detail', kwargs={'site_url': self.site_url})


```

