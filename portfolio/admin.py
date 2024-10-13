from django.contrib import admin
from django.utils.html import format_html
from . import models



@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(models.Work)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('category', 'image_preview', 'name', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    list_filter = ('category', )

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" />'.format(obj.image.url))
        return "Resim Yok"
