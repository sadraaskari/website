# Generated by Django 4.1.6 on 2023-02-14 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0003_alter_payment_payment_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='craeted_at',
            new_name='created_at',
        ),
    ]