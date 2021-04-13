# Generated by Django 3.1.7 on 2021-03-27 06:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='post contents')),
                ('created_on', models.DateTimeField(db_index=True, default=datetime.datetime(2021, 3, 27, 6, 35, 8, 902576), verbose_name='creation time')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
