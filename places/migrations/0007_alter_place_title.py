# Generated by Django 4.1.1 on 2022-09-05 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_alter_image_options_alter_image_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
