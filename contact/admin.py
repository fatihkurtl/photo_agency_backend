from django.contrib import admin
from .models import ContactForm, ContactInformation, SocialMedia, WhyChooseUs, FrequentlyAskedQuestions


@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'phone', 'service', 'date', 'time', 'created_at', 'updated_at')
    search_fields = ('firstname', 'lastname', 'email', 'phone', 'service')
    list_filter = ('service', 'created_at', 'updated_at')
    readonly_fields = ('firstname', 'lastname', 'email', 'phone', 'service', 'date', 'time', 'content', 'created_at', 'updated_at')

@admin.register(ContactInformation)
class ContactInformationAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'address', 'work_hours', 'created_at', 'updated_at')
    search_fields = ('email', 'phone')
    list_filter = ('work_hours',)
    readonly_fields = ('created_at', 'updated_at')

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'created_at', 'updated_at')
    search_fields = ('name',)
    readonly_fields = ('created_at', 'updated_at')

@admin.register(WhyChooseUs)
class WhyChooseUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
    readonly_fields = ('created_at', 'updated_at')

@admin.register(FrequentlyAskedQuestions)
class FrequentlyAskedQuestionsAdmin(admin.ModelAdmin):
    list_display = ('question', 'created_at', 'updated_at')
    search_fields = ('question',)
    readonly_fields = ('created_at', 'updated_at')
