# Generated by Django 5.1.4 on 2024-12-13 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_userprofile_last_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
