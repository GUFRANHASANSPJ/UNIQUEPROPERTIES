# Generated by Django 5.0.7 on 2024-11-07 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0018_populationmix_property_population_mix_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='population_mix',
        ),
        migrations.AddField(
            model_name='property',
            name='population_mix',
            field=models.JSONField(blank=True, default=list),
        ),
    ]
