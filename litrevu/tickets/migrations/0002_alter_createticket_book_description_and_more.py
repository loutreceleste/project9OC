# Generated by Django 4.2.6 on 2023-11-24 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createticket',
            name='book_description',
            field=models.CharField(default='', max_length=2048),
        ),
        migrations.AlterField(
            model_name='createticket',
            name='book_title',
            field=models.CharField(default='', max_length=128),
        ),
    ]