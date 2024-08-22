from django.contrib import admin

from .models import Product, Category, File


@admin.register(Category)
class categoryadmin(admin.ModelAdmin):
    list_display=['title', 'description', 'is_enable', 'time_create']
    list_filter=['title', 'time_create']
    search_fields=['title']


class fileadmin(admin.StackedInline):
    model=File
    list_display=['title', 'time_create']
    list_filter=['title', 'time_create']
    search_fields=['title']
    extra=0

@admin.register(Product)
class productadmin(admin.ModelAdmin):
    list_display=['title', 'is_enable', 'time_create']
    list_filter=['title', 'time_create']
    search_fields=['title']
    filter_horizontal=['categories']
    inlines=[fileadmin]
