# Generated by Django 2.1.4 on 2019-02-21 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20190220_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagefromdirector',
            name='image',
            field=models.ImageField(null=True, upload_to='image'),
        ),
        migrations.AlterField(
            model_name='sliderpicture',
            name='image',
            field=models.ImageField(upload_to='image'),
        ),
    ]