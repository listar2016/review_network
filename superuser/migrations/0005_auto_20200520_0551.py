# Generated by Django 2.1 on 2020-05-20 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superuser', '0004_order_product_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]