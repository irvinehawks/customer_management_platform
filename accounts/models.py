from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length = 200, null = True)
    email = models.CharField(max_length = 200, null = True)
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length = 200, null = True)

class Product(models.Model):

    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
    )
    name = models.CharField(max_length = 200, null = True)
    price = models.CharField(max_length = 200, null = True)
    category = models.CharField(max_length = 200, null = True, choices = CATEGORY)
    description = models.CharField(max_length = 200, null = True)
    date_created = models.DateTimeField(auto_now_add = True)
    tags = models.ManyToManyField(Tag)

class Order(models.Model):

    STATUS = (
        ('Pending', 'Pending'),
        ('Out Of Delivery', 'Out Of Delivery'),
        ('Delivery', 'Delivery'),
    )
    customer = models.ForeignKey(Customer, null = True, on_delete = models.SET_NULL)
    product = models.ForeignKey(Product, null = True, on_delete = models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length = 200, null = True, choices = STATUS)