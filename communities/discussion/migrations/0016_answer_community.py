# Generated by Django 2.2 on 2019-04-09 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0001_initial'),
        ('discussion', '0015_auto_20190409_2320'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='community',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='communities.Community'),
        ),
    ]