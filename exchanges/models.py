from django.db import models


# Create your models here.
class ExchangeType(object):
    Missions = 'Missions'
    Visitors = 'Visitors'


class Exchange(models.Model):
    title = models.TextField()
    content = models.TextField(null=True)
    views_number = models.IntegerField(null=True)
    image = models.TextField(null=True)
    sliderFlag = models.BooleanField(default=False)
    type = models.CharField(max_length=10)
    create_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cn_rise_exchange'
