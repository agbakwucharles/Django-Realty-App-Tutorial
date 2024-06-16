from django.contrib import admin
from .models import Listing

#class is to display extra info on listings
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'isPublished', 'price','list_date','realtor')

    #lets you make text links
    list_display_links = ('id', 'title')


    #lets you filter in admin
    list_filter = ('realtor',)

    #allows checkboxes on booleans
    list_editable = ('isPublished',)

    #can add search field for items
    search_fields = ('title','description','address','city','state','zipcode','price')

    list_per_page = 25






admin.site.register(Listing, ListingAdmin)
