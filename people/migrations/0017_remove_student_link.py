# Generated by Django 2.1.4 on 2019-03-08 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0016_auto_20190308_1016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='link',
        ),
    ]