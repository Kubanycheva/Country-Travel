# Generated by Django 5.1.4 on 2024-12-19 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0007_rename_home_description_home_comment_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attractionculture',
            old_name='comment',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='attractionshome',
            old_name='comment',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='home',
            old_name='comment',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='homereview',
            old_name='comment',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='popularregion',
            old_name='comment',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='popularreview',
            old_name='description',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='region',
            old_name='comment',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='totry',
            old_name='description',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='attractionculture',
            name='description',
        ),
        migrations.RemoveField(
            model_name='attractionshome',
            name='description',
        ),
        migrations.RemoveField(
            model_name='home',
            name='description',
        ),
        migrations.RemoveField(
            model_name='homereview',
            name='description',
        ),
        migrations.RemoveField(
            model_name='popularregion',
            name='description',
        ),
        migrations.RemoveField(
            model_name='region',
            name='description',
        ),
        migrations.RemoveField(
            model_name='totry',
            name='to_name',
        ),
        migrations.AddField(
            model_name='totry',
            name='name',
            field=models.CharField(default=1, max_length=52),
            preserve_default=False,
        ),
    ]
