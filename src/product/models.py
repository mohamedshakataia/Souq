from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class jumia(models.Model):
    title = models.CharField(max_length=300, blank=True, null=True)
    manufacture = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField()
    img = models.TextField()
    url = models.TextField()
    sku = models.CharField(max_length=50, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    lastprice = models.CharField(max_length=50, blank=True, null=True)
    rate = models.FloatField()
    category=models.ForeignKey('Category',verbose_name="category", related_name="category",on_delete=models.CASCADE)

 
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'jumia'


class Category(models.Model):
    sweetName=models.CharField(max_length=50, null=False,unique=True)

    
    def __str__(self):
        return self.sweetName

    class Meta:
        db_table = 'category'