# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markupfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20150903_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='_description_rendered',
            field=models.TextField(default='', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gallery',
            name='description',
            field=markupfield.fields.MarkupField(default='', blank=True, rendered_field=True, help_text='Markdown is allowed'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='description_markup_type',
            field=models.CharField(choices=[('', '--'), ('html', 'HTML'), ('plain', 'Plain'), ('markdown', 'Markdown')], default='markdown', blank=True, editable=False, max_length=30),
        ),
        migrations.AddField(
            model_name='gallerycomment',
            name='_comment_rendered',
            field=models.TextField(default='', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gallerycomment',
            name='comment_markup_type',
            field=models.CharField(choices=[('', '--'), ('html', 'HTML'), ('plain', 'Plain'), ('markdown', 'Markdown')], default='plain', editable=False, max_length=30),
        ),
        migrations.AlterField(
            model_name='gallerycomment',
            name='comment',
            field=markupfield.fields.MarkupField(rendered_field=True),
        ),
        migrations.AlterField(
            model_name='galleryimage',
            name='notes',
            field=markupfield.fields.MarkupField(default='', blank=True, rendered_field=True, help_text='Markdown is allowed'),
        ),
    ]
