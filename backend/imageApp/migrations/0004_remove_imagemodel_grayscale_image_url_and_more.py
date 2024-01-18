# Generated by Django 4.2 on 2024-01-01 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("imageApp", "0003_imagemodel_grayscale_image_url"),
    ]

    operations = [
        migrations.RemoveField(model_name="imagemodel", name="grayscale_image_url",),
        migrations.AlterField(
            model_name="imagemodel",
            name="grayscale_image",
            field=models.ImageField(blank=True, null=True, upload_to="grayscaled/"),
        ),
    ]
