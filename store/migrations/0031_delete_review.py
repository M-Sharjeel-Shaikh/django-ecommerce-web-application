# Generated by Django 4.1.5 on 2023-01-31 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0030_rename_user_review_review'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
    ]
