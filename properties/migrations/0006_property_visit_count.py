# Generated by Django 5.0.7 on 2024-10-31 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0005_alter_property_owners_delete_property_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='visit_count',
            field=models.IntegerField(default=0),
        ),
    ]
