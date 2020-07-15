# Generated by Django 2.2.13 on 2020-07-14 01:25

import api.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('status', models.BooleanField(default=True)),
                ('env', models.TextField(max_length=50)),
                ('version', models.TextField(max_length=5)),
                ('address', models.TextField(max_length=39, validators=[django.core.validators.validate_ipv4_address])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('last_login', models.DateField(auto_now=True)),
                ('email', models.TextField(max_length=254, validators=[django.core.validators.EmailValidator()])),
                ('password', models.TextField(max_length=50, validators=[django.core.validators.MinLengthValidator(6)])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GroupUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Group')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.TextField(choices=[(0, 'INFO'), (1, 'DEBUG'), (2, 'WARNING'), (3, 'ERROR'), (4, 'CRITICAL')], max_length=20, validators=[api.models.Event.level_validator])),
                ('data', models.TextField(max_length=20)),
                ('arquivado', models.BooleanField(default=False)),
                ('date', models.DateField(auto_now=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Agent')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User')),
            ],
        ),
    ]
