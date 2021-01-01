from django.db import models

class Data(models.Model):
   username=models.CharField(primary_key=True,max_length=10)
   email =models.CharField(max_length=20)
   password1 =models.CharField(max_length=20)
   password2 =models.CharField(max_length=20)
   
   
   class Meta:
      db_table = 'data'
