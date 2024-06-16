from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(isPublished=True)[:3]
    context= {
        'listings':listings
    }
    return render(request, 'pages/index.html',context)


def about(request):
    realtors = Realtor.objects.order_by('-hire_date')

    #GET MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context= {
        'realtor':realtors,
        'mvp':mvp_realtors
    }
    return render(request, 'pages/about.html',context)
