# Generated by Django 4.2 on 2023-04-27 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_messages', '0003_auto_20190617_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
