# Generated by Django 2.1.4 on 2019-03-01 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0007_adjunctprofessor_staff_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adjunctprofessor',
            name='professionalTitle',
            field=models.TextField(null=True),
        ),
    ]
