# Generated by Django 4.0.2 on 2022-02-03 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0020_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='zip_code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
