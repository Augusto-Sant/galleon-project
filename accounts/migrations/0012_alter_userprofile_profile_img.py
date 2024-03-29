# Generated by Django 4.0.5 on 2022-08-21 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_userprofile_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_img',
            field=models.CharField(choices=[('Grey Robot', 'Grey Robot'), ('Purple Robot', 'Purple Robot'), ('Rainbow Robot', 'Rainbow Robot'), ('[(\'Grey Robot\', "{% static \'img/profile1.png\'%}"), (\'Purple Robot\', "{% static \'img/profile2.png\'%}"), (\'Rainbow Robot\', "{% static \'img/profile3.png\'%}")]', 'Profile Image Choices')], default='Grey Robot', max_length=1000),
        ),
    ]
