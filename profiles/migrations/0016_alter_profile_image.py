# Generated by Django 4.2.9 on 2024-09-03 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0015_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../nobody_image_ij7rzz', upload_to='images/'),
        ),
    ]
