from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User, AuctionListing, Bids, Comments, WatchLists, Closed


def index(request):
    if request.method == 'POST':
        title = request.POST['title']
        startingBid = request.POST['startingBid']
        image = request.POST['image']
        category = request.POST['category']
        al = AuctionListing(title=title, startingBid=int(
            startingBid), currentBid=int(
            startingBid), image=image, category=category, user=request.user)
        al.save()

    return render(request, "auctions/index.html", {
        'Listings': AuctionListing.objects.all(),
        'closedlistings': Closed.objects.values_list('item_id', flat=True),

    })


def close(request, pk):
    item = AuctionListing.objects.get(id=pk)
    winner = Bids.objects.get(item=item, bid=item.currentBid).user
    # Closed.objects.all().delete()
    close = Closed(winner=winner, item=item, user=item.user)
    close.save()
    return HttpResponseRedirect(reverse('closelist'))


def closelist(request):
    closed_auction_listings = AuctionListing.objects.filter(
        closed__isnull=False)
    return render(request, "auctions/closelist.html", {
        'Listings': closed_auction_listings
    })


def category(request):
    distinct_categories = AuctionListing.objects.values_list(
        'category', flat=True).distinct()
    distinct_categories = distinct_categories.exclude(category__exact='')
    return render(request, "auctions/category.html", {
        'Listings': distinct_categories,
    })


def category_selected(request, selected_category):
    auction_listings = AuctionListing.objects.filter(
        category=selected_category)
    return render(request, "auctions/category.html", {
        'selected_category': selected_category,
        'auction_listings': auction_listings,
    })


def watchlist(request):
    user = request.user
    if request.method == 'POST':
        if 'submit' in request.POST and request.POST['submit'] == 'Add':
            pk = request.POST['id']
            item = AuctionListing.objects.get(id=pk)
            wl = WatchLists(user=user, item=item)
            wl.save()
        if 'submit' in request.POST and request.POST['submit'] == 'Remove':
            pk = request.POST['id']
            item = AuctionListing.objects.get(id=pk)
            wl = WatchLists.objects.get(user=user, item=item)
            wl.delete()

    watchlist_items = WatchLists.objects.filter(user=user)
    auction_listing_items = AuctionListing.objects.filter(
        id__in=watchlist_items.values('item'))

    return render(request, "auctions/watchlist.html", {
        'Listings': auction_listing_items,
    })


def item(request, pk):
    item = AuctionListing.objects.get(id=pk)
    bidder = Bids.objects.filter(item=item, bid=item.currentBid).first()
    allComments = Comments.objects.filter(item=item).order_by('-time')
    closed = Closed.objects.filter(item=item).first()

    context = {
        'list': item,
        'comments': allComments,
    }
    if bidder:
        context['bidder'] = bidder
    if closed:
        context['closed'] = closed
    return render(request, "auctions/item.html", context)


def bid(request, pk):
    item = AuctionListing.objects.get(id=pk)
    if request.method == 'POST':
        bid = int(request.POST["bid"])
        user = request.user
        if item.currentBid < bid:
            item.currentBid = bid
            item.save()
            bidModel = Bids(user=user, bid=bid, item=item)
            bidModel.save()
    return HttpResponseRedirect(reverse('item', kwargs={'pk': pk}))


def comment(request, pk):
    item = AuctionListing.objects.get(id=pk)
    content = request.GET['comment']
    user = request.user
    comment = Comments(Comment=content, user=user, item=item)
    comment.save()
    return HttpResponseRedirect(reverse('item', kwargs={'pk': pk}))


def create(request):
    return render(request, "auctions/create.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
