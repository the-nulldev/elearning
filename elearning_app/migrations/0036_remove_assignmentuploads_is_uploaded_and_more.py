# Generated by Django 4.2 on 2023-05-12 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearning_app', '0035_alter_assignmentuploads_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignmentuploads',
            name='is_uploaded',
        ),
        migrations.AddField(
            model_name='assignment',
            name='is_uploaded',
            field=models.BooleanField(default=False),
        ),
    ]
