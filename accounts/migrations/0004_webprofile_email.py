# Generated by Django 4.0.5 on 2022-06-25 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_webprofile_remove_userprofile_profile_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='webprofile',
            name='email',
            field=models.EmailField(default='null', max_length=256),
        ),
    ]
