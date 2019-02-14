# Generated by Django 2.1.4 on 2018-12-27 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Introduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(null=True)),
                ('content', models.TextField(null=True)),
                ('research_category', models.TextField()),
                ('views_number', models.IntegerField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'cn_rise_introduction',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.TextField()),
                ('title', models.TextField()),
                ('project_code', models.TextField()),
                ('project_fund', models.TextField(null=True)),
                ('project_schedule', models.TextField(null=True)),
                ('other', models.TextField(null=True)),
                ('abstract', models.TextField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'cn_rise_projects',
            },
        ),
        migrations.CreateModel(
            name='Publications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.TextField()),
                ('title', models.TextField()),
                ('public_place', models.TextField()),
                ('public_year', models.TextField()),
                ('other', models.TextField(null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'cn_rise_publications',
            },
        ),
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.TextField()),
                ('title', models.TextField()),
                ('report_place', models.TextField()),
                ('report_time', models.TextField()),
                ('report_year', models.TextField()),
                ('pdf_path', models.TextField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'cn_rise_reports',
            },
        ),
    ]