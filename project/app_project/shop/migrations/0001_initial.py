# Generated by Django 5.0.2 on 2024-02-12 07:11

import django.db.models.deletion
import shop.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('status', models.BooleanField(default=False, help_text='0-show,1-hidden')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('vendor', models.CharField(max_length=150)),
                ('quantity', models.IntegerField()),
                ('orginal_price', models.FloatField()),
                ('selling_price', models.FloatField()),
                ('product_image', models.ImageField(blank=True, null=True, upload_to=shop.models.getfilename)),
                ('description', models.TextField(max_length=500)),
                ('status', models.BooleanField(default=False, help_text='0-show,1-hidden')),
                ('trending', models.BooleanField(default=False, help_text='0-default,1-trending')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.catagory')),
            ],
        ),
    ]
