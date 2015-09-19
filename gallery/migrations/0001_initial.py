# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit_autosuggest.managers
from django.conf import settings
import sorl.thumbnail.fields
import markupfield.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name_plural': 'galleries',
            },
        ),
        migrations.CreateModel(
            name='GalleryComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('date', models.DateTimeField()),
                ('comment', models.TextField()),
            ],
            options={
                'ordering': ['image', 'user'],
            },
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to='gallery')),
                ('notes', markupfield.fields.MarkupField(blank=True, default='', rendered_field=True)),
                ('notes_markup_type', models.CharField(editable=False, blank=True, choices=[('', '--'), ('html', 'HTML'), ('plain', 'Plain'), ('markdown', 'Markdown')], default='markdown', max_length=30)),
                ('_notes_rendered', models.TextField(editable=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('sort_order', models.PositiveIntegerField(default=0, db_index=True, editable=False)),
                ('gallery', models.ForeignKey(to='gallery.Gallery')),
            ],
            options={
                'ordering': ['sort_order'],
            },
        ),
        migrations.CreateModel(
            name='LocationTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name='Name')),
                ('slug', models.SlugField(unique=True, max_length=100, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Location',
            },
        ),
        migrations.CreateModel(
            name='MiscTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name='Name')),
                ('slug', models.SlugField(unique=True, max_length=100, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Misc',
            },
        ),
        migrations.CreateModel(
            name='PeopleTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name='Name')),
                ('slug', models.SlugField(unique=True, max_length=100, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'People',
            },
        ),
        migrations.CreateModel(
            name='PhotographerTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name='Name')),
                ('slug', models.SlugField(unique=True, max_length=100, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Photographer',
            },
        ),
        migrations.CreateModel(
            name='TaggedLocations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('object_id', models.IntegerField(db_index=True, verbose_name='Object id')),
                ('content_type', models.ForeignKey(related_name='gallery_taggedlocations_tagged_items', verbose_name='Content type', to='contenttypes.ContentType')),
                ('tag', models.ForeignKey(to='gallery.LocationTag', related_name='location')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaggedMisc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('object_id', models.IntegerField(db_index=True, verbose_name='Object id')),
                ('content_type', models.ForeignKey(related_name='gallery_taggedmisc_tagged_items', verbose_name='Content type', to='contenttypes.ContentType')),
                ('tag', models.ForeignKey(to='gallery.MiscTag', related_name='tags')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaggedPeople',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('object_id', models.IntegerField(db_index=True, verbose_name='Object id')),
                ('content_type', models.ForeignKey(related_name='gallery_taggedpeople_tagged_items', verbose_name='Content type', to='contenttypes.ContentType')),
                ('tag', models.ForeignKey(to='gallery.PeopleTag', related_name='people')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaggedPhotographer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('object_id', models.IntegerField(db_index=True, verbose_name='Object id')),
                ('content_type', models.ForeignKey(related_name='gallery_taggedphotographer_tagged_items', verbose_name='Content type', to='contenttypes.ContentType')),
                ('tag', models.ForeignKey(to='gallery.PhotographerTag', related_name='photographer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='location',
            field=taggit_autosuggest.managers.TaggableManager(help_text='A comma-separated list of tags.', blank=True, to='gallery.LocationTag', through='gallery.TaggedLocations', verbose_name='Location'),
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='people',
            field=taggit_autosuggest.managers.TaggableManager(help_text='A comma-separated list of tags.', blank=True, to='gallery.PeopleTag', through='gallery.TaggedPeople', verbose_name='People'),
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='photographer',
            field=taggit_autosuggest.managers.TaggableManager(help_text='A comma-separated list of tags.', blank=True, to='gallery.PhotographerTag', through='gallery.TaggedPhotographer', verbose_name='Photographer'),
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='tags',
            field=taggit_autosuggest.managers.TaggableManager(help_text='A comma-separated list of tags.', blank=True, to='gallery.MiscTag', through='gallery.TaggedMisc', verbose_name='Tags'),
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
