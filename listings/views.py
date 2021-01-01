from django.shortcuts import render,get_object_or_404

from .models import Listings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .choice import price_choices,bedroom_choices,state_choices

def index(request):

    listings = Listings.objects.filter(is_published=True)
    paginator = Paginator(listings,1)
    page = request.GET.get('page',1)
    try:
        paged_listings = paginator.page(page)
    except PageNotAnInteger:
         paged_listings = paginator.page(1)
    except EmptyPage:
         paged_listings = paginator.page(paginator.num_pages)

    
    
    
    
    context = {
        "listings":paged_listings
    }

    return render(request,'listings/listings.html',context)


def listing(request,id =None ):
    list = get_object_or_404(Listings,id = id)
    context = {
        "listings":list
    }
    return render(request,'listings/listing.html',context)


def search(request):
    query_list = Listings.objects.order_by('-list_date')

    # keyword

    if "keyword" in request.GET:
        keyword = request.GET["keyword"]
        if keyword:
            query_list = query_list.filter(description__icontains=keyword)

    if "city" in request.GET:
        city = request.GET["city"]
        if city:
            query_list = query_list.filter(city__iexact=city)

    if "state" in request.GET:
        state = request.GET["city"]
        if state:
            query_list = query_list.filter(state__iexact=state)
    
    if "bedrooms" in request.GET:
        bedrooms = request.GET["bedrooms"]
        if bedrooms:
            print("here")
            query_list = query_list.filter(bedrooms__iexact=bedrooms)
    

    if "price" in request.GET:
        price = request.GET["price"]
        if price:
            query_list = query_list.filter(price__lte=price)

    print(query_list)
    context={
        "state_choice":state_choices,
        "price_choice":price_choices,
        "listings":query_list,
        'bedroom_choices': bedroom_choices,
        "values":request.GET
    }

    return render(request,"listings/search.html",context)