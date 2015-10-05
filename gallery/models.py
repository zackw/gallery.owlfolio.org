from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from sorl.thumbnail import ImageField
from adminsortable.fields import SortableForeignKey
from adminsortable.models import SortableMixin
from markupfield.fields import MarkupField
from taggit_autosuggest.managers import TaggableManager
# from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase
from taggit.models import GenericTaggedItemBase, TagBase

import os

class LocationTag(TagBase):
    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'
class TaggedLocations(GenericTaggedItemBase):
    tag = models.ForeignKey('LocationTag', related_name='location')

class PeopleTag(TagBase):
    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'
class TaggedPeople(GenericTaggedItemBase):
    tag = models.ForeignKey('PeopleTag', related_name = "people")

class MiscTag(TagBase):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
class TaggedMisc(GenericTaggedItemBase):
    tag = models.ForeignKey('MiscTag', related_name = "tags")

class PhotographerTag(TagBase):
    class Meta:
        verbose_name = 'Photographer'
        verbose_name_plural = 'Photographers'
class TaggedPhotographer(GenericTaggedItemBase):
    tag = models.ForeignKey('PhotographerTag', related_name = "photographer")

class Gallery(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    description = MarkupField(markup_type='markdown', default='', blank=True, help_text="Markdown is allowed")

    class Meta:
        verbose_name_plural = "galleries"

    def __str__(self):
        return self.title

def image_upload_path(instance, filename):
    return os.path.join(instance.gallery.slug, filename)

class GalleryImage(SortableMixin):
    gallery = models.ForeignKey(Gallery)
    image = ImageField(upload_to=image_upload_path)
    notes = MarkupField(markup_type='markdown', default='', blank=True, help_text="Markdown is allowed")
    location = TaggableManager('Location', through=TaggedLocations, blank=True)
    people = TaggableManager('People', through=TaggedPeople, blank=True)
    tags = TaggableManager('Tags', through=TaggedMisc, blank=True)
    photographer = TaggableManager('Photographer', through=TaggedPhotographer, blank=True)
    date = models.DateTimeField(default=timezone.now)
    # ordering
    sort_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    order_field_name = 'sort_order'

    class Meta:
        ordering = ['sort_order']

    def __str__(self):
        return str(self.image)

class GalleryComment(models.Model):
    image = models.ForeignKey(GalleryImage)
    user = models.ForeignKey(User)
    date = models.DateTimeField()
    comment = MarkupField(markup_type='markdown')

    def is_published_version(self):
        return GalleryComment.objects.filter(image=self.image, user=self.user, date__gt=self.date).count() == 0
    # is_published_version.admin_order_field = 'date'
    is_published_version.boolean = True
    is_published_version.short_description = 'Published version?'

    class Meta:
        ordering = ['image', 'user']

    def __str__(self):
        return self.comment
