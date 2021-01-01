from django.shortcuts import render,redirect
from . import forms
# Create your views here.

from .models import Contact

def contact(request):
    if request.method=="POST":
        #

        form = forms.ContactForm(request.POST)
        listing_id = request.POST.get('listings_id',None)
        print(request.POST)
        if form.is_valid():
                form.save(commit=True)
        
        return redirect('/listings/'+listing_id)
