from rest_framework.serializers import ModelSerializer

from .models import Product, PurchaseProduct

class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ["id", "name", "unit", "stock_quantity", "average_purchase_price", "selling_price"]