# Generated by Django 4.1.5 on 2023-02-04 07:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0034_alter_review_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='averagerating',
        ),
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
    ]