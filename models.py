from django.db import models

# Create your models here.
class Category(models.Model):
    cat_name=models.CharField(max_length=30)
    class Meta:
        db_table="Category"
        
class Flight(models.Model):
    name=models.CharField(max_length=40)
    price=models.IntegerField(default=5000)
    description=models.CharField(max_length=100)
    way = models.CharField(max_length=50)
    ImageUrl=models.ImageField(upload_to="Images",default="MyFligt.jpg")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    class Meta:
        db_table="Flight"
