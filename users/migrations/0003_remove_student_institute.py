# Generated by Django 4.1.6 on 2023-04-04 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_role_permission'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='institute',
        ),
    ]