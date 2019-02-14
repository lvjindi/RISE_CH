# Generated by Django 2.1.4 on 2018-12-27 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MessageFromDirector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(null=True)),
                ('title', models.TextField(default='Message from the Director', null=True)),
                ('image', models.TextField(null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'cn_rise_message',
            },
        ),
        migrations.CreateModel(
            name='SliderPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flag', models.TextField(default=1)),
                ('image', models.TextField()),
                ('articleId', models.TextField(null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'cn_rise_slider',
            },
        ),
    ]