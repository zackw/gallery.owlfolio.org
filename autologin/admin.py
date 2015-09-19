from django.contrib import admin

from .models import AutoLogin

class AutoLoginAdmin(admin.ModelAdmin):
    list_display = ('user', 'token')

admin.site.register(AutoLogin, AutoLoginAdmin)