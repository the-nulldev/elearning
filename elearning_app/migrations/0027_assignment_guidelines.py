# Generated by Django 4.2 on 2023-04-28 11:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("elearning_app", "0026_rename_to_be_submitted_by_examtest_deadline_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="assignment",
            name="guidelines",
            field=models.TextField(
                default="Submit to the following email", max_length=1024
            ),
            preserve_default=False,
        ),
    ]
