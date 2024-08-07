# Generated by Django 4.2.9 on 2024-07-03 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmedialink',
            name='platform',
            field=models.CharField(choices=[('facebook', 'Facebook'), ('instagram', 'Instagram'), ('youtube', 'YouTube'), ('website', 'Website')], max_length=50),
        ),
        migrations.AlterField(
            model_name='socialmedialink',
            name='url',
            field=models.URLField(),
        ),
    ]
