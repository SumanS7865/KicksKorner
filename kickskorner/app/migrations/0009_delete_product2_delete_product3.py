# Generated by Django 4.1.7 on 2023-05-02 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_product3'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product2',
        ),
        migrations.DeleteModel(
            name='Product3',
        ),
    ]