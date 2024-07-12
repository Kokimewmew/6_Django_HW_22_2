from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLED


def get_product_from_cache():
    """Получает данные по собакам из кэша, если кэш пуст, получает данные из бд"""
    if not CACHE_ENABLED:
        return Product.objects.all()

    key = "product_list"
    product = cache.get(key)
    if product is not None:
        return product

    product = Product.objects.all()

    cache.get(key, product)
    return product





