# Generated by Django 3.2.18 on 2023-03-25 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0029_rename_listingcategory_listing_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Listing_Category',
            new_name='Category',
        ),
    ]