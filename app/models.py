from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField(default=0) 
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return '{} - {}'.format(self.name, self.price)
    
    
class Purchase(models.Model):
    product_purchased = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    change_returned = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Bought:{} Change Returned:{} On:{}'.format(self.product_purchased, self.change_returned, self.created)
    

    
class Attempt(models.Model):
    coins_inserted = models.CharField(max_length=300)
    product_selected = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    
    
