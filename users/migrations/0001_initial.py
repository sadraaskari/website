# Generated by Django 4.1.6 on 2023-02-14 01:19

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
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('father_name', models.CharField(default='', max_length=30)),
                ('phone', models.IntegerField(default=0)),
                ('online_or_offline', models.IntegerField(default=0)),
                ('profile_picture', models.ImageField(blank=True, upload_to='profile_pictures')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.role')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major', models.IntegerField(default=0)),
                ('grade', models.IntegerField(default=0)),
                ('institute', models.CharField(default='', max_length=30)),
                ('school', models.CharField(default='', max_length=30)),
                ('mother_phone', models.IntegerField(default=0)),
                ('father_phone', models.IntegerField(default=0)),
                ('home_phone', models.IntegerField(default=0)),
                ('support_id', models.IntegerField(default=0)),
                ('counselor_id', models.IntegerField(default=0)),
                ('manager_id', models.IntegerField(default=0)),
                ('support_name', models.CharField(default='', max_length=30)),
                ('counselor_name', models.CharField(default='', max_length=30)),
                ('manager_name', models.CharField(default='', max_length=30)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.userprofile')),
            ],
        ),
    ]
