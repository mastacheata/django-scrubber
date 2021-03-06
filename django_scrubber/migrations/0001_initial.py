# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-24 08:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FakeData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.CharField(db_index=True, max_length=255, verbose_name='Faker provider')),
                ('provider_offset', models.PositiveSmallIntegerField()),
                ('content', models.CharField(max_length=255, verbose_name='Fake content')),
            ],
        ),
        migrations.AddIndex(
            model_name='fakedata',
            index=models.Index(fields=['provider', 'provider_offset'], name='django_scru_provide_d7f250_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='fakedata',
            unique_together=set([('provider', 'provider_offset')]),
        ),
    ]
