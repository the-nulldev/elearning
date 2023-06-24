# Generated by Django 4.2 on 2023-05-12 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elearning_app', '0036_remove_assignmentuploads_is_uploaded_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assignmentscores',
            options={'verbose_name_plural': 'Assignment Scores'},
        ),
        migrations.CreateModel(
            name='PastAssignments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finished_assignment_file', models.FileField(upload_to='assignment/uploads')),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning_app.assignment')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning_app.student')),
            ],
        ),
    ]
