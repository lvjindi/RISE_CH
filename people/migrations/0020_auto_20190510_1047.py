# Generated by Django 2.1.4 on 2019-05-10 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0019_staff_linkname'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['type', 'name']},
        ),
    ]
