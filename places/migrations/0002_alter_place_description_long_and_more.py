# Generated by Django 4.1.1 on 2023-02-01 21:34

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=tinymce.models.HTMLField(blank=True),
        ),
    ]