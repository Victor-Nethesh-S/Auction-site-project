# Generated by Django 4.2.3 on 2023-07-24 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auctionlisting_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='bids',
            name='bids',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='bids',
            name='item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auctions.auctionlisting'),
        ),
        migrations.AddField(
            model_name='comments',
            name='Comments',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='comments',
            name='item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auctions.auctionlisting'),
        ),
    ]
