# Generated by Django 3.2.9 on 2021-12-26 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='genre',
            field=models.ManyToManyField(related_name='genre', to='books.Genre'),
        ),
    ]