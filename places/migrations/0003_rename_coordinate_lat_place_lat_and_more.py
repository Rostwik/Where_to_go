# Generated by Django 4.1.1 on 2023-02-01 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_alter_place_description_long_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='coordinate_lat',
            new_name='lat',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='coordinate_lng',
            new_name='lon',
        ),
    ]
