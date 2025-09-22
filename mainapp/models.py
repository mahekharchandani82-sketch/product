from django.db import models

# Create your models here.

class Notification(models.Model):
    image = models.ImageField(upload_to='media/')
    about = models.TextField()
    def __str__(self):
        return self.about
    
class order_list(models.Model):
    order = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    operator = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    distance = models.CharField(max_length=100)
    start_date = models.CharField(max_length=100)
    est_delivery = models.CharField(max_length=100)
    
    def __str__(self):
        return self.order
    
class Product_Add(models.Model):
    CATEGORY_CHOICES = [
        ('New Arrival', 'New Arrival'),
        ('Most Popular', 'Most Popular'),
        ('Trending', 'Trending'),
    ]

    name=models.CharField(max_length=255)
    description=models.CharField(max_length=255,null=True,blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='new',null=True,blank=True)
    expire=models.DateField()
    stock=models.IntegerField()
    photo=models.ImageField(null=True,blank=True, upload_to="media")
    
class Catagory(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Sign(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100,null=True,blank=True)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username