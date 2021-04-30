from django.contrib import admin
from .models import Tutorial

class TtAdmin(admin.ModelAdmin):
    list_display = ('title', 'update')
    list_display_links = ('title',)
    search_fields = ('title', 'content')

admin.site.register(Tutorial, TtAdmin)
