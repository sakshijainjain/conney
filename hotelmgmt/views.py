from django.shortcuts import render ,redirect
from .forms import RoomBookingForm , FoodOrderForm
# Create your views here.

def hotel(request):
	return render(request ,'hotelmgmt/hotelfront.html')



def roomBook(request):
	if request.method=='POST':
		form  = RoomBookingForm(request.POST)

		if form.is_valid():
			form.save(commit=True)
		return redirect('https://paytm.com/')



	form  = RoomBookingForm()

	return render(request , 'hotelmgmt/roomDetails.html',{"form":form})

def foodorder(request):
	if request.method=='POST':
		form  = FoodOrderForm(request.POST)

		if form.is_valid():
			form.save(commit=True)
		return redirect('https://paytm.com/')



	form  = FoodOrderForm()

	return render(request , 'hotelmgmt/foodDetails.html',{"form":form})
