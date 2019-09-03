from django.db import models

# Create your models here.
from django.utils import timezone


class News(models.Model):
    title = models.TextField()
    content = models.TextField(null=True)
    views_number = models.IntegerField(default=0)
    image = models.ImageField(upload_to='image/')
    sliderFlag = models.BooleanField(default=False)
    type = models.TextField(null=True)
    create_time = models.DateTimeField(default=timezone.now())
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cn_rise_news'
