# Generated by Django 3.0.4 on 2020-04-24 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_auto_20200423_2058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request_contact',
            old_name='request_id',
            new_name='ar_id',
        ),
        migrations.RenameField(
            model_name='request_datetime',
            old_name='request_id',
            new_name='ar_id',
        ),
    ]
