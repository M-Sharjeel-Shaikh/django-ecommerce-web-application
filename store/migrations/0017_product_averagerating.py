# Generated by Django 4.1.5 on 2023-01-29 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_alter_product_information_alter_product_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='averagerating',
            field=models.FloatField(default=0),
        ),
    ]