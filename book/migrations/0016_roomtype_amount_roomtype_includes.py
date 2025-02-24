# Generated by Django 4.2.11 on 2025-01-09 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0015_price_includes'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomtype',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='roomtype',
            name='includes',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
