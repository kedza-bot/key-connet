from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_top', 'created_at')
    list_filter = ('is_top', 'created_at')
    search_fields = ('title', 'short_description')
