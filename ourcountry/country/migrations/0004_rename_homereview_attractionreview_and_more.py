# Generated by Django 5.1.4 on 2024-12-19 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0003_reviewimage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HomeReview',
            new_name='AttractionReview',
        ),
        migrations.RenameModel(
            old_name='PopularRegion',
            new_name='PopularPlaces',
        ),
    ]