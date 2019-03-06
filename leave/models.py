from django.db import models


# Create your models here.

class Leave(models.Model):
    name = models.TextField()
    email = models.TextField()
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    reason = models.TextField()
    status = models.TextField(default='审核中')
    create_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cn_rise_leave'
