# Generated by Django 2.2 on 2019-04-09 20:48

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('discussion', '0011_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply_on_Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('time', models.TimeField(default=datetime.datetime.now)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discussion.Comment')),
                ('creator', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reply_on_Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('time', models.TimeField(default=datetime.datetime.now)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discussion.Answer')),
                ('creator', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
