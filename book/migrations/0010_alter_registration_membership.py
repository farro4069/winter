# Generated by Django 4.2.11 on 2024-04-20 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0009_registration_membership'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='membership',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='book.membership'),
        ),
    ]
