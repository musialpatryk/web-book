# Generated by Django 3.2.9 on 2021-12-05 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='book_images'),
        ),
    ]
