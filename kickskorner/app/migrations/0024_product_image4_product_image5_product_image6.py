# Generated by Django 4.1.7 on 2023-05-05 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_product_image3'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image4',
            field=models.ImageField(blank=True, upload_to='photos/products'),
        ),
        migrations.AddField(
            model_name='product',
            name='image5',
            field=models.ImageField(blank=True, upload_to='photos/products'),
        ),
        migrations.AddField(
            model_name='product',
            name='image6',
            field=models.ImageField(blank=True, upload_to='photos/products'),
        ),
    ]
