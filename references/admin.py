from django.contrib import admin
from django.utils.html import format_html
from .models import CustomerPortfolio, CustomerTestimonials, FeaturedProjects, SectoralRecognition


@admin.register(CustomerPortfolio)
class CustomerPortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo_preview', 'created_at', 'updated_at')
    search_fields = ('name',)
    readonly_fields = ('created_at', 'updated_at')
    
    
    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="100" height="100" />'.format(obj.logo.url))
        return "Logo Yok"
    

@admin.register(CustomerTestimonials)
class CustomerTestimonialsAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'image_preview', 'created_at', 'updated_at')
    search_fields = ('name', 'company')
    readonly_fields = ('created_at', 'updated_at')
    
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" />'.format(obj.image.url))
        return "Resim Yok"
    

@admin.register(FeaturedProjects)
class FeaturedProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_preview', 'created_at', 'updated_at')
    search_fields = ('title',)
    readonly_fields = ('created_at', 'updated_at')
    
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" />'.format(obj.image.url))
        return "Resim Yok"


@admin.register(SectoralRecognition)
class SectoralRecognitionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at')
    search_fields = ('title',)
    readonly_fields = ('created_at', 'updated_at')