# Generated by Django 2.1.4 on 2019-03-15 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0003_leave_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='status',
            field=models.TextField(choices=[('agree', '同意'), ('disagree', '拒绝'), ('audit', '审核中')], default='audit'),
        ),
    ]
