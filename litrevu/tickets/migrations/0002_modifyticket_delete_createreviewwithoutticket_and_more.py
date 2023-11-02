# Generated by Django 4.2.6 on 2023-11-02 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModifyTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(default='', max_length=100)),
                ('book_description', models.CharField(default='', max_length=100)),
                ('book_image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='CreateReviewWithoutTicket',
        ),
        migrations.DeleteModel(
            name='CreateReviewWithTicket',
        ),
    ]
