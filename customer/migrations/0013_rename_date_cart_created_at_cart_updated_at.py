# Generated by Django 4.2.3 on 2023-08-26 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0012_alter_favourite_favourite_alter_favourite_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='date',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='cart',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
