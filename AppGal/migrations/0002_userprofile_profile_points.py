# Generated by Django 4.0.5 on 2022-06-25 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppGal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_points',
            field=models.PositiveIntegerField(default=0, verbose_name='ship_coins'),
        ),
    ]
