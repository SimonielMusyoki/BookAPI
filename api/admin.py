from django.contrib import admin
from .models import Book, BookNumber, Character, Author


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # fields = ('title',)
    list_display = ['title', 'description', 'price']
    search_fields = ['title', 'description']
    list_filter = ['published']


admin.site.register(BookNumber)
admin.site.register(Character)
admin.site.register(Author)
