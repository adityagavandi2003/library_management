from django.contrib import admin
from book.models import Book,Author,Category
# Register your models here.

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Category)