# Generated by Django 3.0.4 on 2020-03-18 00:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0005_payout_request_task_worker'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='claimed_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
