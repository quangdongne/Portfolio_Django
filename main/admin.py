from django.contrib import admin
from . models import (UserProfile, ContactProfile, Testimonial, Service,
                      Service_Detail, Skill, Qualification, Media, Portfolio)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'location')


@admin.register(ContactProfile)
class ContactProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'timestamp')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    readonly_fields = ('slug',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_active')


@admin.register(Service_Detail)
class ServiceDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Qualification)
class QualificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'sort_id', 'title',
                    'sub_title', 'year_from', 'year_to')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'sort_id', 'name', 'score')

# Register your models here.
