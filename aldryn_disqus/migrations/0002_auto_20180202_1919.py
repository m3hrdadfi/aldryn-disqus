# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_disqus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisqusService',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('shortname', models.CharField(verbose_name='Shortname', max_length=100, blank=True, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='disqusplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(primary_key=True, to='cms.CMSPlugin', related_name='aldryn_disqus_disqusplugin', serialize=False, auto_created=True, parent_link=True),
        ),
        migrations.AddField(
            model_name='disqusplugin',
            name='disqus',
            field=models.ForeignKey(to='aldryn_disqus.DisqusService', on_delete=django.db.models.deletion.SET_NULL, blank=True, verbose_name='Disqus Service', null=True),
        ),
    ]
