# Generated by Django 4.1.3 on 2022-12-22 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suggestions', '0026_alter_questionarymodel_diet_meal_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionarymodel',
            name='diet_meal_quantity',
            field=models.CharField(choices=[('always on diet', 'Always'), ('1 time', 'One'), ('2 times', 'Two'), ('3 times', 'Three'), ('4 times', 'Four'), ('has no any diet', 'Never')], default=None, max_length=256),
        ),
        migrations.AlterField(
            model_name='questionarymodel',
            name='on_a_diet',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default=None, max_length=3),
        ),
        migrations.AlterField(
            model_name='questionarymodel',
            name='phisical_exercises',
            field=models.CharField(choices=[('Yes, and more then 2 hours per week', 'Yes More 2H'), ('Yes, but less then 2 hours per week', 'Yes Less 2H'), ('No, I do not do any phisical exercises', 'No')], default=None, max_length=256),
        ),
        migrations.AlterField(
            model_name='questionarymodel',
            name='physical_activity',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default=None, max_length=3),
        ),
        migrations.AlterField(
            model_name='suggestionmodel',
            name='forecast',
            field=models.CharField(default=None, max_length=256),
        ),
        migrations.AlterField(
            model_name='suggestionmodel',
            name='suggestion',
            field=models.CharField(default=None, max_length=256),
        ),
    ]
