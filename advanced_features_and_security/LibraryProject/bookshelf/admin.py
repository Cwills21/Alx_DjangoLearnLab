# from django.contrib import admin
# from .models import Book

# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     # Columns to display in the list view
#     list_display = ('title', 'author', 'publication_year')

#     # Filters on the right side
#     list_filter = ('publication_year', 'author')

#     # Search bar fields
#     search_fields = ('title', 'author')
# bookshelf/admin.py
from django.contrib import admin
from .models import CustomUser  # register your CustomUser instead of Book

admin.site.register(CustomUser)
