# Generated by Django 5.1.2 on 2024-11-04 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredient', '0002_ingredient_date_purchased_ingredient_expiry_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]