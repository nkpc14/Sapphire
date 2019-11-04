# Generated by Django 2.2.6 on 2019-10-10 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registerform', '0004_auto_20191009_2132'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalTeamRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=100)),
                ('college_name', models.CharField(max_length=100)),
                ('college_address', models.CharField(max_length=300)),
                ('captain_name', models.CharField(max_length=100)),
                ('captain_registration_number', models.IntegerField()),
                ('aadhar_number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', models.IntegerField()),
                ('vice_captain_name', models.CharField(max_length=100)),
                ('vice_captain_registration_number', models.IntegerField()),
                ('vice_aadhar_number', models.IntegerField()),
                ('vice_email', models.EmailField(max_length=254)),
                ('vice_contact_number', models.IntegerField()),
                ('player_name3', models.CharField(max_length=100)),
                ('player_registration_number3', models.IntegerField()),
                ('player_name4', models.CharField(max_length=100)),
                ('player_registration_number4', models.IntegerField()),
                ('player_name5', models.CharField(max_length=100)),
                ('player_registration_number5', models.IntegerField()),
                ('player_name6', models.CharField(max_length=100)),
                ('player_registration_number6', models.IntegerField()),
                ('player_name7', models.CharField(max_length=100)),
                ('player_registration_number7', models.IntegerField()),
                ('player_name8', models.CharField(max_length=100)),
                ('player_registration_number8', models.IntegerField()),
                ('player_name9', models.CharField(max_length=100)),
                ('player_registration_number9', models.IntegerField()),
                ('player_name10', models.CharField(max_length=100)),
                ('player_registration_number10', models.IntegerField()),
                ('player_name11', models.CharField(max_length=100)),
                ('player_registration_number11', models.IntegerField()),
                ('player_name12', models.CharField(max_length=100)),
                ('player_registration_number12', models.IntegerField()),
                ('player_name13', models.CharField(max_length=100)),
                ('player_registration_number13', models.IntegerField()),
                ('player_name14', models.CharField(max_length=100)),
                ('player_registration_number14', models.IntegerField()),
                ('player_name15', models.CharField(max_length=100)),
                ('player_registration_number15', models.IntegerField()),
                ('payment_id', models.CharField(blank=True, max_length=255, null=True)),
                ('accommodation', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='InternalTeamRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=100)),
                ('captain_name', models.CharField(max_length=100)),
                ('captain_registration_number', models.IntegerField()),
                ('captain_reg', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', models.IntegerField()),
                ('vice_captain_name', models.CharField(max_length=100)),
                ('vice_captain_registration_number', models.IntegerField()),
                ('vice_caption_reg', models.IntegerField()),
                ('vice_email', models.EmailField(max_length=254)),
                ('vice_contact_number', models.IntegerField()),
                ('player_name3', models.CharField(max_length=100)),
                ('player_registration_number3', models.IntegerField()),
                ('player_name4', models.CharField(max_length=100)),
                ('player_registration_number4', models.IntegerField()),
                ('player_name5', models.CharField(max_length=100)),
                ('player_registration_number5', models.IntegerField()),
                ('player_name6', models.CharField(max_length=100)),
                ('player_registration_number6', models.IntegerField()),
                ('player_name7', models.CharField(max_length=100)),
                ('player_registration_number7', models.IntegerField()),
                ('player_name8', models.CharField(max_length=100)),
                ('player_registration_number8', models.IntegerField()),
                ('player_name9', models.CharField(max_length=100)),
                ('player_registration_number9', models.IntegerField()),
                ('player_name10', models.CharField(max_length=100)),
                ('player_registration_number10', models.IntegerField()),
                ('player_name11', models.CharField(max_length=100)),
                ('player_registration_number11', models.IntegerField()),
                ('player_name12', models.CharField(max_length=100)),
                ('player_registration_number12', models.IntegerField()),
                ('player_name13', models.CharField(max_length=100)),
                ('player_registration_number13', models.IntegerField()),
                ('player_name14', models.CharField(max_length=100)),
                ('player_registration_number14', models.IntegerField()),
                ('player_name15', models.CharField(max_length=100)),
                ('player_registration_number15', models.IntegerField()),
                ('payment_id', models.CharField(blank=True, max_length=255, null=True)),
                ('accommodation', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='RegisterForm',
        ),
    ]