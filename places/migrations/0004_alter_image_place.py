# Generated by Django 4.1.1 on 2023-02-05 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_rename_coordinate_lat_place_lat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.place'),
        ),
    ]
