# Generated by Django 4.2 on 2023-06-08 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_category_added_by_category_course_category_subject_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, help_text='a description of the category', verbose_name='Description'),
        ),
    ]
