# Generated by Django 3.0.3 on 2020-02-18 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200218_2217'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_pic',
            new_name='image',
        ),
    ]
