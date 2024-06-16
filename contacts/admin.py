from .models import Contact
from django.contrib import admin

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name','listing','email','contact_date')
    list_display_links = ('id','name')
    list_per_page = 25
    search_fields = ('name','email','listing')

admin.site.register(Contact,ContactAdmin)
