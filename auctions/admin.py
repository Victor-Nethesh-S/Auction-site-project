from django.contrib import admin
from .models import AuctionListing, Bids, Comments, WatchLists, Closed

# Register your models here.
admin.site.register(AuctionListing)
admin.site.register(Bids)
admin.site.register(Comments)
admin.site.register(WatchLists)
admin.site.register(Closed)
