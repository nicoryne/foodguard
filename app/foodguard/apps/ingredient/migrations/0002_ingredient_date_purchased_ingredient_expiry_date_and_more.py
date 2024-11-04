# Generated by Django 5.1.2 on 2024-11-04 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredient', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='date_purchased',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='expiry_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='quantity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='ingredients/'),
        ),
    ]
