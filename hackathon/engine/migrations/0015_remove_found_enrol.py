# Generated by Django 4.1.4 on 2023-01-13 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0014_remove_lost_enrol'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='found',
            name='enrol',
        ),
    ]
