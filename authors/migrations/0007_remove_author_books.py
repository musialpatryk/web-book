# Generated by Django 3.2.9 on 2021-11-20 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0006_author_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='books',
        ),
    ]