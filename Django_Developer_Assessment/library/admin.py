from django.contrib import admin
from .models import authorm, bookm 

# Register your models here.

@admin.register(authorm)
class authoradmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'adress']


@admin.register(bookm)
class bookadmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'pb_year', 'isbn', 'price']

