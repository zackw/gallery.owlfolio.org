# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit_autosuggest.managers
import markupfield.fields
import django.utils.timezone
import sorl.thumbnail.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('description', markupfield.fields.MarkupField(default='', blank=True, help_text='Markdown is allowed')),
                ('description_markup_type', models.CharField(blank=True, choices=[('', '--'), ('html', 'html'), ('plain', 'plain'), ('markdown', 'markdown')], max_length=30, default='markdown', editable=False)),
                ('_description_rendered', models.TextField(editable=False)),
            ],
            options={
                'verbose_name_plural': 'galleries',
            },
        ),
        migrations.CreateModel(
            name='GalleryComment',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('comment', markupfield.fields.MarkupField()),
                ('comment_markup_type', models.CharField(choices=[('', '--'), ('html', 'html'), ('plain', 'plain'), ('markdown', 'markdown')], max_length=30, default='plain', editable=False)),
                ('_comment_rendered', models.TextField(editable=False)),
            ],
            options={
                'ordering': ['image', 'user'],
            },
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to='gallery')),
                ('notes', markupfield.fields.MarkupField(default='', blank=True, help_text='Markdown is allowed')),
                ('notes_markup_type', models.CharField(blank=True, choices=[('', '--'), ('html', 'html'), ('plain', 'plain'), ('markdown', 'markdown')], max_length=30, default='markdown', editable=False)),
                ('_notes_rendered', models.TextField(editable=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('sort_order', models.PositiveIntegerField(db_index=True, default=0, editable=False)),
                ('gallery', models.ForeignKey(to='gallery.Gallery')),
            ],
            options={
                'ordering': ['sort_order'],
            },
        ),
        migrations.CreateModel(
            name='LocationTag',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='Name', unique=True, max_length=100)),
                ('slug', models.SlugField(verbose_name='Slug', unique=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Locations',
                'verbose_name': 'Location',
            },
        ),
        migrations.CreateModel(
            name='MiscTag',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='Name', unique=True, max_length=100)),
                ('slug', models.SlugField(verbose_name='Slug', unique=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Tags',
                'verbose_name': 'Tag',
            },
        ),
        migrations.CreateModel(
            name='PeopleTag',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='Name', unique=True, max_length=100)),
                ('slug', models.SlugField(verbose_name='Slug', unique=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'People',
                'verbose_name': 'Person',
            },
        ),
        migrations.CreateModel(
            name='PhotographerTag',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='Name', unique=True, max_length=100)),
                ('slug', models.SlugField(verbose_name='Slug', unique=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Photographers',
                'verbose_name': 'Photographer',
            },
        ),
        migrations.CreateModel(
            name='TaggedLocations',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('object_id', models.IntegerField(db_index=True, verbose_name='Object id')),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType', related_name='gallery_taggedlocations_tagged_items', verbose_name='Content type')),
                ('tag', models.ForeignKey(to='gallery.LocationTag', related_name='location')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaggedMisc',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('object_id', models.IntegerField(db_index=True, verbose_name='Object id')),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType', related_name='gallery_taggedmisc_tagged_items', verbose_name='Content type')),
                ('tag', models.ForeignKey(to='gallery.MiscTag', related_name='tags')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaggedPeople',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('object_id', models.IntegerField(db_index=True, verbose_name='Object id')),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType', related_name='gallery_taggedpeople_tagged_items', verbose_name='Content type')),
                ('tag', models.ForeignKey(to='gallery.PeopleTag', related_name='people')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaggedPhotographer',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('object_id', models.IntegerField(db_index=True, verbose_name='Object id')),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType', related_name='gallery_taggedphotographer_tagged_items', verbose_name='Content type')),
                ('tag', models.ForeignKey(to='gallery.PhotographerTag', related_name='photographer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='location',
            field=taggit_autosuggest.managers.TaggableManager(blank=True, through='gallery.TaggedLocations', help_text='A comma-separated list of tags.', to='gallery.LocationTag', verbose_name='Location'),
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='people',
            field=taggit_autosuggest.managers.TaggableManager(blank=True, through='gallery.TaggedPeople', help_text='A comma-separated list of tags.', to='gallery.PeopleTag', verbose_name='People'),
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='photographer',
            field=taggit_autosuggest.managers.TaggableManager(blank=True, through='gallery.TaggedPhotographer', help_text='A comma-separated list of tags.', to='gallery.PhotographerTag', verbose_name='Photographer'),
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='tags',
            field=taggit_autosuggest.managers.TaggableManager(blank=True, through='gallery.TaggedMisc', help_text='A comma-separated list of tags.', to='gallery.MiscTag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='gallerycomment',
            name='image',
            field=models.ForeignKey(to='gallery.GalleryImage'),
        ),
        migrations.AddField(
            model_name='gallerycomment',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
