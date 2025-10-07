from django.contrib import admin

from main import models
from main.models import ImageModel, Post


# Register your models here.
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_admin')

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'is_published')

@admin.register(models.ImageModel)
class ImageModelAdmin(admin.ModelAdmin):
    list_display = ('post', 'index')


# class ImageInline(admin.TabularInline):
#     model = ImageModel
#     extra = 1
#
#
# class PostModelAdmin(admin.ModelAdmin):
#     inlines = [ImageInline]
#
#
# admin.site.register(Post, PostModelAdmin)