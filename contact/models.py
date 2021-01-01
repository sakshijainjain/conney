from django.db import models

# Create your models here.
from datetime import datetime

class Contact(models.Model):
    listings = models.CharField(max_length=200)
    listings_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now(),blank=True)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.name