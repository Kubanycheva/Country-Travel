# Generated by Django 5.1.4 on 2024-12-16 09:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0004_alter_favoriteregion_user_favoritehotel_hotelsregion_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kitchen',
            old_name='kitchen_description',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='kitchen',
            name='culture_kitchen',
        ),
        migrations.AddField(
            model_name='kitchen',
            name='kitchen_region',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='hotels_region_image', to='country.region'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hotelsregion',
            name='hotels_region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotels_region', to='country.region'),
        ),
        migrations.AlterField(
            model_name='kitchen',
            name='kitchen_name',
            field=models.CharField(max_length=155),
        ),
        migrations.CreateModel(
            name='FavoriteKitchen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kitchen_favorite', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kitchen_regions', to='country.region')),
            ],
        ),
        migrations.CreateModel(
            name='KitchenReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('client_kitchen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kitchen_reviews', to=settings.AUTH_USER_MODEL)),
                ('kitchen_region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='country.kitchen')),
            ],
        ),
    ]