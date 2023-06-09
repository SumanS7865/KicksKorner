from django.db import models
from category.models import Category
from django.urls import reverse


# Create your models here.
    
class Product(models.Model):
    product_name            = models.CharField(max_length=200, unique=True)
    slug                    = models.SlugField(max_length=200, unique=True)
    description             = models.TextField(max_length=1000, blank=True)
    selling_price           = models.CharField(max_length=50)
    discounted_price        = models.CharField(max_length=50, blank=True)
    product_detail_ribbon   =models.CharField(max_length=50,blank=True)
    ribbon                  = models.CharField(max_length=20, blank=True)
    image1                  = models.ImageField(upload_to='photos/products')
    image2                  = models.ImageField(upload_to='photos/products')
    image3                  = models.ImageField(upload_to='photos/products', blank=True)
    image4                  = models.ImageField(upload_to='photos/products', blank=True)
    image5                  = models.ImageField(upload_to='photos/products', blank=True)
    image6                  = models.ImageField(upload_to='photos/products', blank=True)
    stock                   = models.IntegerField()
    is_available            = models.BooleanField(default=True)
    category                = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date            = models.DateTimeField(auto_now_add=True)
    modified_date           =models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name


    

