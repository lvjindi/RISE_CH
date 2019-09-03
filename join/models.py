from django.db import models

# Create your models here.
from django.utils import timezone


class Join(models.Model):
    title = models.TextField()
    content = models.TextField(null=True)
    views_number = models.IntegerField(null=True, default=0)
    image = models.TextField(null=True)
    sliderFlag = models.BooleanField(default=False)
    news_id = models.IntegerField(null=True)
    create_time = models.DateTimeField(default=timezone.now())
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cn_rise_join'
