# Generated by Django 5.1.4 on 2024-12-20 12:50

import multiselectfield.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0011_remove_kitchen_kitchen_image_kitchen_meal_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitchen',
            name='type_of_cafe',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Russian', 'Russian'), ('Asian', 'Asian'), ('Canadian', 'Canadian'), ('Chinese', 'Chinese'), ('European', 'European'), ('Japan', 'Japan'), ('Korean', 'Korean')], default=1, max_length=52),
            preserve_default=False,
        ),
    ]