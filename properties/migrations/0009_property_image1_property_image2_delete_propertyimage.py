# Generated by Django 5.0.7 on 2024-11-05 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0008_propertyimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='properties_img/'),
        ),
        migrations.AddField(
            model_name='property',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='properties_img/'),
        ),
        migrations.DeleteModel(
            name='PropertyImage',
        ),
    ]