# Generated by Django 2.1.4 on 2019-04-01 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_auto_20190221_1119'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='messagefromdirector',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='sliderpicture',
            options={'ordering': ['id']},
        ),
    ]
