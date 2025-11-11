from django.contrib import admin

from .models import Product, PurchaseProduct


admin.site.register([Product, PurchaseProduct])