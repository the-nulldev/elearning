# Generated by Django 4.1.7 on 2023-04-26 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elearning_app', '0014_rename_assignment_subject_assignment_subject_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignment',
            old_name='assignment_course',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='exam',
            old_name='exam_course',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='stud_course',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='subject_course',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='teacher_course',
            new_name='course',
        ),
        migrations.AddField(
            model_name='book',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='elearning_app.course'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pastpaper',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='elearning_app.course'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='elearning_app.course'),
            preserve_default=False,
        ),
    ]
