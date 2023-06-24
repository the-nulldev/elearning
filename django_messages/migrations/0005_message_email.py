# Generated by Django 4.2.1 on 2023-06-04 19:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("django_messages", "0004_alter_message_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="email",
            field=models.EmailField(
                blank=True, max_length=254, null=True, verbose_name="Email"
            ),
        ),
    ]
