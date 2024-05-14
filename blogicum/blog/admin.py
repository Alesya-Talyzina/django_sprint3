from django.contrib import admin

from .models import Location, Category, Post

admin.site.empty_value_display = 'не задано'


class PostInline(admin.TabularInline):
    model = Post
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = (PostInline,)
    list_display = ('title',)


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'text',
        'created_at',
        'is_published',
        'pub_date',
        'author',
        'location',
        'category',
    )
    list_editable = (
        'is_published',
        'category',
    )
    search_fields = ('title',)
    list_filter = ('category',)
    list_display_links = ('title',)


admin.site.register(Location)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
