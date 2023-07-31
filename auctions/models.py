from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class AuctionListing(models.Model):
    title = models.CharField(max_length=100)
    startingBid = models.IntegerField(default=0)
    currentBid = models.IntegerField(default=0)
    image = models.URLField(null=True, blank=True, max_length=2000)
    category = models.CharField(max_length=64, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


class Bids(models.Model):
    bid = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item = models.ForeignKey(
        AuctionListing, on_delete=models.CASCADE, default=1)


class Comments(models.Model):
    Comment = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item = models.ForeignKey(
        AuctionListing, on_delete=models.CASCADE, default=1)


class WatchLists(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item = models.ForeignKey(
        AuctionListing, on_delete=models.CASCADE, default=1)


class Closed(models.Model):
    winner = models.ForeignKey(
        User, default=1, on_delete=models.DO_NOTHING, related_name="closed_winner")
    item = models.ForeignKey(
        AuctionListing, default=1, on_delete=models.DO_NOTHING, unique=True)
    user = models.ForeignKey(
        User, default=1, on_delete=models.DO_NOTHING, related_name="closed_user")
