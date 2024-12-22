# Generated by Django 5.1.4 on 2024-12-22 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0022_culturekitchen_remove_currency_culture_currency_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='address',
            field=models.CharField(default=1, max_length=62),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='galleryreview',
            name='rating',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True),
        ),
    ]
