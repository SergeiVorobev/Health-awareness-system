# Generated by Django 4.1.3 on 2023-01-03 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0004_quiz_result_question_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='time',
        ),
    ]
