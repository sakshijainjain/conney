from django import forms
from .models import RoomBooking , FoodOrder


class RoomBookingForm(forms.ModelForm):
	
	class Meta:
		model = RoomBooking
		fields = '__all__'


class FoodOrderForm(forms.ModelForm):
	
	class Meta:
		model = FoodOrder
		fields = '__all__'
