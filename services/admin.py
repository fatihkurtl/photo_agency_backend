from django.contrib import admin
from .models import Category, Package, Service, Feature


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    prepopulated_fields = {'slug': ('name',)}
    

class FeatureInline(admin.TabularInline):
    model = Feature
    extra = 1
    

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'service', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    list_filter = ('service',)
    inlines = [FeatureInline]
    

class PackageInline(admin.TabularInline):
    model = Package
    extra = 1
    show_change_link = True
    

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    list_filter = ('category',)
    inlines = [PackageInline]
    

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('description', 'package', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    list_filter = ('package__service', 'package')