# Generated by Django 2.1.4 on 2019-03-12 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0007_remove_publications_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reports',
            name='pdf_path',
            field=models.FileField(upload_to=''),
        ),
    ]
