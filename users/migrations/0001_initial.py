# Generated by Django 4.1.6 on 2023-02-23 14:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(default='', max_length=30)),
                ('permission', models.JSONField(default=dict)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('major', models.IntegerField(default=0)),
                ('grade', models.IntegerField(default=0)),
                ('institute', models.CharField(default='', max_length=30)),
                ('school', models.CharField(default='', max_length=30)),
                ('mother_phone', models.CharField(default='', max_length=30)),
                ('father_phone', models.CharField(default='', max_length=30)),
                ('home_phone', models.CharField(default='', max_length=30)),
                ('support_id', models.IntegerField(default=0)),
                ('counselor_id', models.IntegerField(default=0)),
                ('manager_id', models.IntegerField(default=0)),
                ('support_name', models.CharField(default='', max_length=30)),
                ('counselor_name', models.CharField(default='', max_length=30)),
                ('manager_name', models.CharField(default='', max_length=30)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('father_name', models.CharField(default='', max_length=30)),
                ('phone', models.CharField(default='', max_length=30, unique=True)),
                ('online_or_offline', models.IntegerField(default=0)),
                ('profile_picture', models.ImageField(blank=True, upload_to='profile_pictures')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('role', models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='users.role')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SumOfStudy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(default=django.utils.timezone.now)),
                ('end_time', models.TimeField(default=django.utils.timezone.now)),
                ('test_count', models.IntegerField(default=0)),
                ('study_time', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True, default='')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('sum_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.student')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.userprofile'),
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.CharField(default='', max_length=30)),
                ('exam_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('exam_score', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('exam_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.student')),
            ],
        ),
    ]
