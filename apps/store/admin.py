from django.contrib import admin

from store.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'authors', 'publisher', 'publication_date', 'description')
    fields = ('title', 'authors', 'publisher', 'publication_date', 'description')
    search_fields = ('title', 'authors', 'publisher', 'publication_date', 'description')
