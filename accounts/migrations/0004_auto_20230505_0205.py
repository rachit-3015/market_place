# Generated by Django 3.2.18 on 2023-05-04 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_user_location_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='clgEmail_is_verified',
        ),
        migrations.RemoveField(
            model_name='user',
            name='clgEmail_token',
        ),
        migrations.RemoveField(
            model_name='user',
            name='clg_email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_location_address',
        ),
    ]
