# Generated by Django 2.2 on 2019-04-10 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnose', '0002_diagnose_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnose',
            name='date_time',
            field=models.DateTimeField(),
        ),
    ]
