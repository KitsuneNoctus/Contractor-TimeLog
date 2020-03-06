# Generated by Django 3.0.2 on 2020-03-05 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TimeLog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='modified',
            field=models.DateTimeField(auto_now=True, help_text='The date and time this page was updated. Automatically generated when the model updates.'),
        ),
        migrations.AlterField(
            model_name='class',
            name='class_description',
            field=models.TextField(help_text='Enter Class Description Here.'),
        ),
        migrations.AlterField(
            model_name='class',
            name='class_name',
            field=models.CharField(help_text='Class Name', max_length=50),
        ),
    ]