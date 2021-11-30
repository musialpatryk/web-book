# Generated by Django 3.2.9 on 2021-11-20 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0003_auto_20211120_1245'),
        ('books', '0002_auto_20211120_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='genre',
            field=models.ManyToManyField(related_name='genre', to='books.Genre'),
        ),
        migrations.AddField(
            model_name='author',
            name='rating',
            field=models.FloatField(default=5.0),
        ),
        migrations.AddField(
            model_name='author',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='description',
            field=models.TextField(default='None'),
        ),
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(default='None', max_length=30),
        ),
        migrations.AlterField(
            model_name='author',
            name='surname',
            field=models.CharField(default='None', max_length=30),
        ),
    ]