# Generated by Django 4.2.11 on 2024-04-20 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_remove_registration_membership'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Membership',
        ),
    ]
