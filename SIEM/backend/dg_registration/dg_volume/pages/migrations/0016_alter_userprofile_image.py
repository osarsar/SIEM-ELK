# Generated by Django 5.0.7 on 2024-07-19 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_alter_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='profile_images/default_profile_image.jpg', null=True, upload_to='profile_images/'),
        ),
    ]