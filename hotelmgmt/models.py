from django.db import models

# Create your models here.

class RoomBooking(models.Model):
	type_room = models.CharField(max_length=20)
	
	duration = models.IntegerField()
	mobileno = models.IntegerField()
	number_of_rooms = models.IntegerField()
	
	

class FoodOrder(models.Model):
	 	
	room_no = models.IntegerField()
	total_amount = models.IntegerField()
	extra_instructions = models.CharField(max_length=50)
		
