# Generated by Django 4.2.9 on 2024-07-04 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_socialmedialink_platform_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='socialmedialink',
            options={'ordering': ['platform']},
        ),
    ]
