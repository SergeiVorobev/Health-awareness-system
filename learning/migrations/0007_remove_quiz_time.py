# Generated by Django 4.1.3 on 2023-01-06 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0006_quiz_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='time',
        ),
    ]
