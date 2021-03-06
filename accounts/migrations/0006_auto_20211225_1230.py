# Generated by Django 3.2.9 on 2021-12-25 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_profile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(default='None', max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile_images/UserDefault.png', upload_to='profile_images'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(default='None', max_length=50),
        ),
    ]
