from django.db import models

# Create your models here.
from django.utils import timezone


class Exchange(models.Model):
    ExchangeType = (
        ('mission', u'出访'),
        ('visitor', u'来访'),
    )
    title = models.TextField()
    content = models.TextField(null=True)
    views_number = models.IntegerField(default=0)
    image = models.TextField(null=True)
    sliderFlag = models.BooleanField(default=False)
    type = models.CharField(choices=ExchangeType, max_length=10)
    news_id = models.IntegerField(null=True)
    create_time = models.DateTimeField(default=timezone.now())
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cn_rise_exchange'
