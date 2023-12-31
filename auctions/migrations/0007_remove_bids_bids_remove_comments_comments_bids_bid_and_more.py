# Generated by Django 4.2.3 on 2023-07-24 06:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_bids_bids_bids_item_comments_comments_comments_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bids',
            name='bids',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='Comments',
        ),
        migrations.AddField(
            model_name='bids',
            name='bid',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bids',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comments',
            name='Comment',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
