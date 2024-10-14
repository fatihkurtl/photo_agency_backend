from django.contrib import admin
from django.utils.html import format_html
from .models import HeroSection



@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image_preview', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" />'.format(obj.image.url))
        return "Resim Yok"
