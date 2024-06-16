from django.shortcuts import render
from .models import Listing
from realtors.models import Realtor
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    #filtering list displayed
    listings = Listing.objects.order_by('-list_date').filter(isPublished=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listing = paginator.get_page(page)
    context = {
        'listings':paged_listing
    }
    return render(request,'listings/listings.html',context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    mvps = Realtor.objects.filter(is_mvp=True)
    context = {
        'listingone': listing,
    }
    return render(request, 'listings/listing.html',context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    #Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    #city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    #state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    #bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    #price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'listings': queryset_list,
        'values': request.GET
    }

    return render(request, 'listings/search.html',context)