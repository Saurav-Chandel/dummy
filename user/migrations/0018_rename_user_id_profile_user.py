# Generated by Django 4.0.2 on 2022-02-03 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_rename_profiles_profile_delete_contactus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='User_id',
            new_name='user',
        ),
    ]
