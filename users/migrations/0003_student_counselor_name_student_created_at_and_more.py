# Generated by Django 4.1.6 on 2023-02-13 10:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_counselor_name_student_counselor_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='counselor_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='student',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='student',
            name='manager_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='student',
            name='support_name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
