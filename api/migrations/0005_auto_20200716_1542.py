# Generated by Django 2.2.13 on 2020-07-16 15:42

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200715_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='level',
            field=models.CharField(choices=[(0, 'INFO'), (1, 'DEBUG'), (2, 'WARNING'), (3, 'ERROR'), (4, 'CRITICAL')], max_length=20, validators=[api.models.Event.level_validator]),
        ),
    ]
