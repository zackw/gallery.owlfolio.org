# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='locationtag',
            options={'verbose_name_plural': 'Locations', 'verbose_name': 'Location'},
        ),
        migrations.AlterModelOptions(
            name='misctag',
            options={'verbose_name_plural': 'Tags', 'verbose_name': 'Tag'},
        ),
        migrations.AlterModelOptions(
            name='peopletag',
            options={'verbose_name_plural': 'People', 'verbose_name': 'Person'},
        ),
        migrations.AlterModelOptions(
            name='photographertag',
            options={'verbose_name_plural': 'Photographers', 'verbose_name': 'Photographer'},
        ),
    ]
