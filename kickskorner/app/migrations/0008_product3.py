# Generated by Django 4.1.7 on 2023-05-02 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_product2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('ribbon', models.CharField(max_length=20)),
                ('image1', models.ImageField(upload_to='')),
                ('image2', models.ImageField(upload_to='')),
            ],
        ),
    ]
