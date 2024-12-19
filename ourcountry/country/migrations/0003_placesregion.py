# Generated by Django 5.1.4 on 2024-12-16 07:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0002_culture_currency_games_handcrafts_kitchen_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlacesRegion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('stars', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='country.placesregion')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='country.region')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
