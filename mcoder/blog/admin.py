from django.contrib import admin
from blog.models import Post, BlogComment, Like, View

admin.site.register((BlogComment, Like, View))
@admin.register(Post)


class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)