# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-27 20:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
            options={
                'db_table': 'content',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=256)),
                ('postdata', models.DateTimeField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
            options={
                'db_table': 'post',
            },
        ),
        migrations.AddField(
            model_name='content',
            name='post',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='post.Post'),
        ),
    ]
