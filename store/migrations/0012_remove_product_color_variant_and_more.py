# Generated by Django 4.1.5 on 2023-01-28 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_alter_product_extra_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='color_variant',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size_variant',
        ),
        migrations.DeleteModel(
            name='ColorVariant',
        ),
        migrations.DeleteModel(
            name='SizeVariant',
        ),
    ]