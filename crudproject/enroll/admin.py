from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password', 'update')
    list_display_links = ('name', 'email')
    list_filter = ('create', 'update')
