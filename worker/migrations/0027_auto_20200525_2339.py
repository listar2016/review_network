# Generated by Django 2.1 on 2020-05-25 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0026_auto_20200525_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payout_request',
            name='order',
            field=models.IntegerField(null=True),
        ),
    ]