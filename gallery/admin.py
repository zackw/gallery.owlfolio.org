from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from adminsortable.admin import NonSortableParentAdmin, SortableTabularInline

from .models import Gallery, GalleryImage, GalleryComment
from .models import LocationTag, PeopleTag, MiscTag, PhotographerTag

class ImageInline(AdminImageMixin, SortableTabularInline):
    model = GalleryImage
    extra = 1
    fields = ('image', 'notes', 'date', 'location', 'people', 'photographer', 'tags')

class GalleryAdmin(NonSortableParentAdmin):
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ImageInline]

class GalleryCommentAdmin(admin.ModelAdmin):
	list_display = ('comment', 'image', 'user', 'date', 'is_published_version')
	list_filter = ['user', 'image']
	search_fields = ['comment']

admin.site.register(Gallery, GalleryAdmin)
admin.site.register(GalleryComment, GalleryCommentAdmin)
# admin.site.register(GalleryImage)

admin.site.register(LocationTag)
admin.site.register(PeopleTag)
admin.site.register(MiscTag)
admin.site.register(PhotographerTag)