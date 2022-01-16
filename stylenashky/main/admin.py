from django.contrib import admin
from .models import Product, Customer, Contact, URL

from import_export.admin import ImportExportActionModelAdmin
from import_export import resources

class ProductResource(resources.ModelResource):


    class Meta:
        model = Product
        fields = ('id','number_product','title','price','stock','massa','stock_in_bag','avg_price')

class ProductAdmin(ImportExportActionModelAdmin):

    resource_class =ProductResource

    list_display = ['title','published_at']
    list_editable = ['published_at',]

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user_tel', 'complete')
    list_editable = ('complete',)


admin.site.register(Product,ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Contact)
admin.site.register(URL)

