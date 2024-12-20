# Generated by Django 5.0.7 on 2024-11-08 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0027_property_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='posted_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='proprty_info',
            field=models.CharField(blank=True, choices=[('1BHK', '1BHK'), ('2BHK', '2BHK'), ('3BHK', '3BHK'), ('4BHK', '4BHK')], default='1BHK', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='proprty_status',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
