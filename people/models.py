from django.db import models


# Create your models here.

class People(models.Model):
    name = models.TextField()
    user_category = models.TextField()# staff, student,adjundt professor
    office = models.TextField(null=True)
    phone = models.TextField(null=True)
    email = models.TextField(null=True)
    profession = models.TextField(null=True)
    position = models.TextField(null=True)
    degree = models.TextField()
    degreeId = models.BigIntegerField()
    professionalTitle = models.TextField()
    area = models.TextField()
    interesting = models.TextField(null=True)
    introduce = models.TextField(null=True)
    project = models.TextField(null=True)
    achievement = models.TextField(null=True)
    activity = models.TextField(null=True)
    papers = models.TextField(null=True)
    report = models.TextField(null=True)
    link = models.TextField(null=True)
    img = models.TextField()
    status = models.BooleanField()
    create_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cn_rise_people'
