# Generated by Django 4.2.11 on 2024-05-31 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0011_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='code',
            field=models.CharField(default='B', max_length=3),
            preserve_default=False,
        ),
    ]
