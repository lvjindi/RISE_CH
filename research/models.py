from django.db import models
from django.utils import timezone


class Category(object):
    Introduction = 'Introduction'
    Projects = 'Projects'
    Publications = 'Publications'
    Reports = 'Reports'


# Create your models here.

class Introduction(models.Model):
    title = models.TextField(null=True)
    content = models.TextField(null=True)
    views_number = models.IntegerField(default=0)
    create_time = models.DateTimeField(default=timezone.now())
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cn_rise_introduction'


class Projects(models.Model):
    author = models.TextField()
    title = models.TextField()
    project_code = models.TextField()
    project_fund = models.TextField(null=True)
    project_schedule = models.TextField(null=True)
    other = models.TextField(null=True)
    abstract = models.TextField()
    keywords = models.TextField(null=True)
    views_number = models.IntegerField(default=0)
    create_time = models.DateTimeField(default=timezone.now())
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cn_rise_projects'


class Publications(models.Model):
    author = models.TextField()
    title = models.TextField()
    place = models.TextField()
    year = models.TextField()
    other = models.TextField(null=True)
    create_time = models.DateTimeField(default=timezone.now())
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cn_rise_publications'


class Reports(models.Model):
    author = models.TextField()
    title = models.TextField()
    place = models.TextField(null=True)
    time = models.TextField(null=True)
    year = models.TextField(null=True)
    pdf_path = models.FileField(null=True)
    other = models.TextField(null=True)
    create_time = models.DateTimeField(default=timezone.now())
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cn_rise_reports'
