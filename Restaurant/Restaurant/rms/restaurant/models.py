from django.db import models

# Create your models here.


class Restaurant(models.Model):
    restaurant_id = models.AutoField
    restaurant_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50,default="")
    subcategory = models.CharField(max_length=50,default="")
    desc = models.CharField(max_length=300)
    start_date = models.DateField()
    image = models.ImageField(upload_to="restaurant/images",default="")

    def __str__(self):
        return self.restaurant_name

class Food(models.Model):
    item_id = models.AutoField
    restaurant_id = models.IntegerField()
    item_name = models.CharField(max_length=200)
    amount = models.IntegerField(default=0)
    image = models.ImageField(upload_to="food/images", default="")

    def __str__(self):
        return self.item_name

class Order(models.Model):
    name = models.CharField(max_length=100)
    item_id = models.IntegerField()
    order_id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.name
