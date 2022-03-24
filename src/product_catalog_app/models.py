from datetime import datetime
from django.db import models
from django.urls import  reverse

import datetime
import os

# Create your models here.



class Category(models.Model):
    name= models.CharField(max_length=50)
    slug = models.SlugField(unique=True)


    class Meta:
           verbose_name_plural = 'Categories'

    @staticmethod
    def get_all_categories():
        return Category.objects.all()
        

    def get_absolute_url(self):
        return reverse('product_catalog_app:product_by_category', args=[self.slug])
    def __str__(self):
        return self.name



def filepath(request,filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%W')
    filename = "%s%s" % (timeNow, old_filename)
    return filename



     

class Product(models.Model):
    """ A Product that will be displayed"""

    name = models.CharField(max_length=200)
    item_number = models.CharField(max_length=200)
    picture = models.ImageField(upload_to=filepath,null=True, blank = True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

   

    

    def __str__ (self):
        return self.name









