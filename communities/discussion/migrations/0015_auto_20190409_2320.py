# Generated by Django 2.2 on 2019-04-09 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discussion', '0014_post_community'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='community',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communities.Community'),
        ),
    ]
