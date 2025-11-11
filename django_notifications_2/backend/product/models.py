from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    unit = models.CharField(max_length=20, default="pcs")
    stock_quantity = models.PositiveSmallIntegerField(default=0)
    average_purchase_price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    selling_price = models.DecimalField(default=0, decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name
    

class PurchaseProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    sku_code = models.CharField(max_length=50, unique=True)
    unit_price = models.PositiveBigIntegerField()
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product) + " " + self.purchase_date.strftime()
    
