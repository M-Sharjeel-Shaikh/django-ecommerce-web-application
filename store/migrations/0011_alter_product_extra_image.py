# Generated by Django 4.1.5 on 2023-01-28 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_product_extra_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='extra_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]