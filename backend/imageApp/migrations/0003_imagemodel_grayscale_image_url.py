# Generated by Django 4.2 on 2023-12-31 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("imageApp", "0002_imagemodel_grayscale_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="imagemodel",
            name="grayscale_image_url",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
