# Generated by Django 4.1.7 on 2023-04-17 12:24

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.PositiveSmallIntegerField(choices=[(1, 'Admin'), (2, 'Teacher'), (3, 'Student')], default=3)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SessionYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_start', models.DateField()),
                ('session_end', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classes_name', models.CharField(max_length=200)),
                ('classes_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning_app.department')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('teacher_name', models.CharField(max_length=200)),
                ('teacher_email', models.EmailField(max_length=200)),
                ('teacher_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning_app.course')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=200)),
                ('subject_code', models.IntegerField()),
                ('subject_books', models.FileField(blank=True, upload_to='books')),
                ('subject_videos', models.FileField(blank=True, upload_to='videos')),
                ('subject_articles', models.FileField(blank=True, upload_to='articles')),
                ('subject_projects', models.FileField(blank=True, upload_to='projects')),
                ('subject_exams', models.FileField(blank=True, upload_to='exams')),
                ('subject_assignments', models.FileField(blank=True, upload_to='assignments')),
                ('subject_papers', models.FileField(blank=True, upload_to='papers')),
                ('subject_cats', models.FileField(blank=True, upload_to='cats')),
                ('subject_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning_app.course')),
                ('subject_teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning_app.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('stud_number', models.IntegerField()),
                ('stud_name', models.CharField(max_length=200)),
                ('stud_email', models.EmailField(max_length=200)),
                ('stud_profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('stud_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning_app.classes')),
                ('stud_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning_app.department')),
                ('stud_school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning_app.school')),
            ],
        ),
        migrations.CreateModel(
            name='HOD',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning_app.school')),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.CharField(max_length=200)),
                ('exam_code', models.IntegerField()),
                ('exam_body', models.PositiveSmallIntegerField(choices=[(1, 'KNEC'), (2, 'KASNEB'), (3, 'Internal')], default=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('exam_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning_app.course')),
                ('exam_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning_app.subject')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning_app.teacher')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='hod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning_app.hod'),
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment_name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DateTimeField(blank=True)),
                ('assignment_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning_app.course')),
                ('assignment_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning_app.subject')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning_app.teacher')),
            ],
        ),
    ]
