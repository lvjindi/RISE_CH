from django.db import models


# Create your models here.

class Conference(models.Model):
    ConferenceType = (
        ('domestic', u'国内'),
        ('foreign', u'国外'),
    )
    title = models.TextField()
    content = models.TextField(null=True)
    views_number = models.IntegerField(default=0)
    image = models.TextField(null=True)
    sliderFlag = models.BooleanField(default=False)
    type = models.CharField(choices=ConferenceType, max_length=10)
    news_id = models.IntegerField(null=True)
    time = models.DateField(null=True)
    place = models.TextField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cn_rise_conference'
