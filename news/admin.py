from django.contrib import admin
from .models import Category, Author, Post, PostCategory, Comment, Subscribes


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("user", "user_rating")


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Comment)
admin.site.register(Subscribes)

