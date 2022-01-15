from django.contrib import admin
from .models import Product, Customer, Contact, URL

from import_export.admin import ImportExportActionModelAdmin
from import_export import resources

class ProductResource(resources.ModelResource):


    class Meta:
        model = Product

class ProductAdmin(ImportExportActionModelAdmin):
# class CalcAdmin(ExportMixin,admin.ModelAdmin):
    resource_class =ProductResource

    list_display = ['title',]

admin.site.register(Product,ProductAdmin)
admin.site.register(Customer)
admin.site.register(Contact)
admin.site.register(URL)