# Generated by Django 4.1.5 on 2023-01-31 09:12

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0029_user_review'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User_Review',
            new_name='Review',
        ),
    ]
