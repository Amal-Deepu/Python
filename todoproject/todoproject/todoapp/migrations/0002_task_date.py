# Generated by Django 4.1.7 on 2024-02-03 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
    ]
