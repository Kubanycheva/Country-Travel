# Generated by Django 5.1.4 on 2024-12-19 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0007_rename_hotels_region_image_hotels_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelsreview',
            name='stars',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True),
        ),
    ]