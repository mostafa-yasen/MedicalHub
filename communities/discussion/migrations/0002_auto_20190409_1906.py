# Generated by Django 2.2 on 2019-04-09 17:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discussion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('time', models.TimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.DeleteModel(
            name='test',
        ),
    ]
