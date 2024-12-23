# Generated by Django 5.1.4 on 2024-12-22 09:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0023_gallery_address_galleryreview_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryreview',
            name='client_gallery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='galleryreview',
            name='gallery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_reviews', to='country.gallery'),
        ),
    ]