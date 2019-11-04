# Generated by Django 2.2.6 on 2019-10-16 18:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('registerform', '0012_auto_20191016_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='internalteamregistration',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='externalteamregistration',
            name='application_id',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
        migrations.AlterField(
            model_name='internalteamregistration',
            name='application_id',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
