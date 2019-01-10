from django.db import models


# Create your models here.
class News(models.Model):
    title = models.TextField()
    content = models.TextField(null=True)
    views_number = models.IntegerField(null=True)
    image = models.TextField(null=True)
    sliderFlag = models.BooleanField(default=False)
    is_important = models.BooleanField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cn_rise_news'
