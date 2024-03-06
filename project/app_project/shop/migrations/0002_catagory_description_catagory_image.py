# Generated by Django 5.0.2 on 2024-02-14 05:53

import shop.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catagory',
            name='description',
            field=models.TextField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='catagory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=shop.models.getfilename),
        ),
    ]
