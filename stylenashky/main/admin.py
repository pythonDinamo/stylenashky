from django.contrib import admin
from .models import Product, Customer, Contact, URL

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('phone', 'complete')
    list_editable = ('complete',)

admin.site.register(Product)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Contact)
admin.site.register(URL)

