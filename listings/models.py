from django.db import models
from datetime import datetime
from realtors import models as m

# Create your models here.

class Listings(models.Model):
    realtors = models.ForeignKey(m.Realtors,on_delete=models.DO_NOTHING,null=True)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length = 100)
    zipcode = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms  = models.IntegerField()
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5,decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/')
    photo_1 = models.ImageField(upload_to='photos/' )
    photo_2 = models.ImageField(upload_to='photos/' )
    photo_3 = models.ImageField(upload_to='photos/' )
    photo_4 = models.ImageField(upload_to='photos/' )
    photo_5 = models.ImageField(upload_to='photos/' )
    photo_6 = models.ImageField(upload_to='photos/' )
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now,blank=True)
    

    def __str__(self):
        return self.title

