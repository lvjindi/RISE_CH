# Generated by Django 2.1.4 on 2019-03-15 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0003_join_news_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='join',
            name='views_number',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
