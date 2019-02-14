from django.db import models


# Create your models here.
class Seminars(models.Model):
    title = models.TextField()
    content = models.TextField(null=True)
    views_number = models.IntegerField(default=0)
    image = models.ImageField(upload_to="images")
    news_id = models.IntegerField(null=True)
    sliderFlag = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cn_rise_seminars'
