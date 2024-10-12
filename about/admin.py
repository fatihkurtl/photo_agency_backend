from django.contrib import admin
from django.utils.html import format_html
from .models import AboutUsContent, OurApproach, BusinessCard, SkilsAndExperience, Achievements


@admin.register(AboutUsContent)
class AboutUsContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(OurApproach)
class OurApproachAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
    readonly_fields = ('created_at', 'updated_at')
    

@admin.register(BusinessCard)
class BusinessCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'logo_preview', 'created_at', 'updated_at')
    search_fields = ('title', 'subtitle')
    readonly_fields = ('created_at', 'updated_at')

    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="100" height="100" />'.format(obj.logo.url))
        return "Logo Yok"

    logo_preview.short_description = "Logo Önizlemesi"


@admin.register(SkilsAndExperience)
class SkilsAndExperienceAdmin(admin.ModelAdmin):
    list_display = ('content', 'created_at', 'updated_at')
    search_fields = ('content',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Achievements)
class AchievementsAdmin(admin.ModelAdmin):
    list_display = ('year', 'content', 'created_at', 'updated_at')
    search_fields = ('year', 'content')
    readonly_fields = ('created_at', 'updated_at')
