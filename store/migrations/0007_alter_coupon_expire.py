# Generated by Django 4.1.5 on 2023-01-25 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_coupon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='expire',
            field=models.DateTimeField(auto_now=True),
        ),
    ]