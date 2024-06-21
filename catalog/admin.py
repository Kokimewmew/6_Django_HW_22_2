from django.contrib import admin
from catalog.models import Product, Category, Blog


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price", "category")
    list_filter = ("category",)
    search_fields = ("title", "desk",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "title")

