# Generated by Django 2.2 on 2019-04-09 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discussion', '0003_post_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
