# Generated by Django 4.0.5 on 2022-06-12 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.ImageField(default='mainapp/food_images/food.png', upload_to='mainapp/food_images/'),
        ),
    ]
