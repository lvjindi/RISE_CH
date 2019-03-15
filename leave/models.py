from django.db import models


# Create your models here.

class Leave(models.Model):
    StatusType = (
        ('agree', u'同意'),
        ('disagree', u'拒绝'),
        ('audit', u'审核中'),
    )
    name = models.TextField()
    email = models.TextField()
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    reason = models.TextField()
    status = models.TextField(choices=StatusType, default='audit')
    reply = models.TextField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cn_rise_leave'
