from django.shortcuts import render
from listings.models import Listings
from realtors.models import Realtors
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




def index(request):
    listings = Listings.objects.filter(is_published=True)[:3]
    context = {
        'listings':listings
    }
    
    return render(request,'pages/index.html',context)


def about(request):
    info = Realtors.objects.all()
    seller_of_month = Realtors.objects.get(is_mvp=True)
    print(seller_of_month)
    context = {
        'realtors':info,
        'seller_of_month':seller_of_month
    }
    return render(request,'pages/about.html',context)

    
