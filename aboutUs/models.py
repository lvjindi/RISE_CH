from django.db import models


# Create your models here.
class AboutUs(models.Model):
    title = models.TextField()
    content = models.TextField(null=True)
    views_number = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cn_rise_about'
