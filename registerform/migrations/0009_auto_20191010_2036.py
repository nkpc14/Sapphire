# Generated by Django 2.2.6 on 2019-10-10 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registerform', '0008_remove_internalteamregistration_vice_caption_reg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='externalteamregistration',
            name='captain_registration_number',
        ),
        migrations.RemoveField(
            model_name='externalteamregistration',
            name='vice_captain_registration_number',
        ),
    ]
