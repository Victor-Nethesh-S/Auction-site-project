# Generated by Django 4.2.3 on 2023-07-22 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auctionlisting_startingbid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='image',
            field=models.URLField(blank=True, max_length=2000, null=True),
        ),
    ]