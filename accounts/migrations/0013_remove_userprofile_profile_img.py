# Generated by Django 4.0.5 on 2022-08-21 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_userprofile_profile_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_img',
        ),
    ]