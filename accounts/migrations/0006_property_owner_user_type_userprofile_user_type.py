# Generated by Django 5.0.7 on 2024-10-26 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_property_owner_user_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='property_owner',
            name='user_type',
            field=models.CharField(choices=[('regular', 'Regular User'), ('owner', 'Property Owner')], default='regular', max_length=10),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(choices=[('regular', 'Regular User'), ('owner', 'Property Owner')], default='regular', max_length=10),
        ),
    ]