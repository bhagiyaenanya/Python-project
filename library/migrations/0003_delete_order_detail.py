# Generated by Django 4.1.7 on 2023-04-04 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_book_details_order_detail'),
    ]

    operations = [
        migrations.DeleteModel(
            name='order_detail',
        ),
    ]