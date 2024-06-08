from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Category)

class ProductImageAdmin(admin.StackedInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name','price']
    inlines = [ProductImageAdmin]

@admin.register(ColorVariant)
class ColorVariantAdmin(admin.ModelAdmin):
    list_display = ['color_name' ,'price']
    model = ColorVariant

    def __str__(self) -> str:
        return self.color_name

@admin.register(SizeVariant)
class SizeVariantAdmin(admin.ModelAdmin):
    list_display = ['size_name' , 'price']
    model = SizeVariant

    def __str__(self) -> str:
        return self.size_name

admin.site.register(Product,ProductAdmin)

admin.site.register(ProductImage)

