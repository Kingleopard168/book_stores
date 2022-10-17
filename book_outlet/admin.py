from http.cookies import BaseCookie
import imp
from django.contrib import admin

from.models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    #readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Book, BookAdmin)