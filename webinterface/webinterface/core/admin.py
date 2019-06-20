from django.contrib import admin

# Register your models here.
from .models import Product, ProductType
from .models import Bug, BugStatusType, BugProductStatus, Product

admin.site.register(ProductType)

#admin.site.register(Product)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'version', 'product_type')


admin.site.register(BugStatusType)
@admin.register(BugProductStatus)
class BugProductStatusAdmin(admin.ModelAdmin):
    list_display = ('status','bug','product','bsc')

@admin.register(Bug)
class BugAdmin(admin.ModelAdmin):
    list_display =  ('name', 'description', 'get_products', 'user', 'c_date')

    def get_products(self, obj):
        data = obj.product.all()
        return "\n".join([p.name for p in data ])
