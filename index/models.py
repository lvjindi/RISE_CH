# -*-coding:utf-8 -*-
from django.db import models


class SliderPicture(models.Model):
    flag = models.TextField(default=1)
    image = models.ImageField()
    imagePath = models.TextField(null=True)
    articleId = models.TextField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cn_rise_slider'



class MessageFromDirector(models.Model):
    content = models.TextField(null=True)
    title = models.TextField(default='Message from the Director', null=True)
    image = models.ImageField(null=True)
    imagePath = models.TextField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cn_rise_message'
        ordering = ['id']
