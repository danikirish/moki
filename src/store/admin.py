from django.contrib import admin

from store.models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "discount")
    list_filter = ("name", "price", "discount")
    search_fields = ("name", "price", "discount")
    prepopulated_fields = {"slug": ("name",)}

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
