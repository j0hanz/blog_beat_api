# Generated by Django 5.1 on 2024-09-03 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../nobody_image_ij7rzz', upload_to='images/'),
        ),
    ]
