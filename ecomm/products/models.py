from django.db import models
from base.models import *
from django.utils.text import slugify

# Create your models here.

class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug=models.SlugField(unique=True,null=True,blank=True)
    category_image = models.ImageField(upload_to="categories")

    def save(self , *args , **kwargs):
        self.slug = slugify(self.title)
        super(Category,self).save(*args,**kwargs)


class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    #slug is for seo optimization for our own comfortable urls
    slug=models.SlugField(unique=True,null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name= "products")
    price = models.IntegerField()
    product_desciption = models.TextField()

class ProductImage(BaseModel):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product_images")
    image = models.ImageField(upload_to="product")
    