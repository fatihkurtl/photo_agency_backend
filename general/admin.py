from django.contrib import admin
from django.utils.html import format_html
from .models import General, Offer, Seo


@admin.register(General)
class GeneralAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'logo_preview', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    
    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="50" height="50" />', obj.logo.url)
        return "Logo Yok"
    

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
 
 
@admin.register(Seo)
class SeoAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'ogImage_preview', 'twitterImage_preview', 'description', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    
    def ogImage_preview(self, obj):
        if obj.ogImage:
            return format_html('<img src="{}" width="50" height="50" />', obj.ogImage.url)
        return "Logo Yok"
    
    def twitterImage_preview(self, obj):
        if obj.twitterImage:
            return format_html('<img src="{}" width="50" height="50" />', obj.twitterImage.url)
        return "Logo Yok"