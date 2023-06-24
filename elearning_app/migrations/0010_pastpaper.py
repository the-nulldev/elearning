# Generated by Django 4.2 on 2023-04-24 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("elearning_app", "0009_video"),
    ]

    operations = [
        migrations.CreateModel(
            name="PastPaper",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("paper_code", models.IntegerField()),
                ("paper_year", models.DateField()),
                (
                    "paper_subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="elearning_app.subject",
                    ),
                ),
            ],
        ),
    ]
