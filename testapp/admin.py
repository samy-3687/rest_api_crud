from django.contrib import admin
from testapp.models import Products

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['prdid', 'prdname', 'prdcat', 'prdspec', 'prdprice']

admin.site.register(Products, ProductAdmin)
