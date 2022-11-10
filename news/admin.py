from django.contrib import admin
from .models import Category, Author, Post, PostCategory, Comment, Subscribes


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("user", "user_rating")


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "add_time", "author", "post_rating")


admin.site.register(Author, AuthorAdmin)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
admin.site.register(Comment)
admin.site.register(Subscribes)

