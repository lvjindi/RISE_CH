from django.db import models


class Category(object):
    Introduction = 'Introduction'
    Projects = 'Projects'
    Publications = 'Publications'
    Reports = 'Reports'


# Create your models here.

class Introduction(models.Model):
    title = models.TextField(null=True)
    content = models.TextField(null=True)
    research_category = models.TextField()
    views_number = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
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
    create_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cn_rise_projects'


class Publications(models.Model):
    author = models.TextField()
    title = models.TextField()
    public_place = models.TextField()
    public_year = models.TextField()
    other = models.TextField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cn_rise_publications'


class Reports(models.Model):
    author = models.TextField()
    title = models.TextField()
    report_place = models.TextField()
    report_time = models.TextField()
    report_year = models.TextField()
    pdf_path = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cn_rise_reports'
