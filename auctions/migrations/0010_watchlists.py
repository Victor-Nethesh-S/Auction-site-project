# Generated by Django 4.2.3 on 2023-07-24 09:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_auctionlisting_currentbid'),
    ]

    operations = [
        migrations.CreateModel(
            name='WatchLists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auctions.auctionlisting')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
