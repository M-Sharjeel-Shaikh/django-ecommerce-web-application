# Generated by Django 4.1.5 on 2023-01-25 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_productimage_product_review'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Coupon',
        ),
    ]