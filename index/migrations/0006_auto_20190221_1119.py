# Generated by Django 2.1.4 on 2019-02-21 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_auto_20190221_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagefromdirector',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='sliderpicture',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]