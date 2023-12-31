# Generated by Django 4.2.3 on 2023-07-22 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auctionlisting_bids_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlisting',
            name='startingBid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='auctionlisting',
            name='category',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
