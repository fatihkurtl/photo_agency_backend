from django.contrib import admin
from .models import ServiceContent, Category, Package, Service, Feature, WhyChooseOurServices



@admin.register(ServiceContent)
class ServiceContentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('name',)
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    search_help_text = 'Kategori adına göre arama yapabilirsiniz.'
    

class FeatureInline(admin.TabularInline):
    model = Feature
    extra = 1
    

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'service', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    list_filter = ('service',)
    search_fields = ('name', 'service__title')
    search_help_text = 'Paket adına ve hizmet adına göre arama yapabilirsiniz.'
    inlines = [FeatureInline]
    

class PackageInline(admin.TabularInline):
    model = Package
    extra = 1
    show_change_link = True
    

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'active', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    list_filter = ('category', 'active')
    list_editable = ('active',)
    search_fields = ('title', 'category__name')
    search_help_text = 'Başlık veya kategori adına göre arama yapabilirsiniz.' 
    inlines = [PackageInline]
    

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('description', 'package', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    list_filter = ('package__service', 'package')
    search_fields = ('description', 'package__name')
    search_help_text = 'Özellik adına ve paket adına arama yapabilirsiniz.'
    

@admin.register(WhyChooseOurServices)
class WhyChooseOurServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('title',)
    search_help_text = 'Başlığa göre arama yapabilirsiniz.'