from django.contrib import admin
from django.db import IntegrityError

from .models import Product, Customer, Contact, URL

from import_export.admin import ImportExportActionModelAdmin
from import_export import resources


class ProductResource(resources.ModelResource):
    set_unique = set()

    class Meta:
        model = Product
        fields = ('id','number_product','title','price','stock','massa','stock_in_bag','avg_price')
        skip_unchanged = True
        report_skipped = True

    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
        self.set_unique = set()


    def skip_row(self, instance, original):
        number_product = instance.number_product
        title = instance.title
        tuple_unique = (number_product, title)

        if tuple_unique in self.set_unique:
            return True
        else:
            self.set_unique.add(tuple_unique)

        return super(ProductResource, self).skip_row(instance, original)

    def save_instance(self, instance, using_transactions=True, dry_run=False):
        try:
            super(ProductResource, self).save_instance(instance, using_transactions, dry_run)
        except IntegrityError:
            pass


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

