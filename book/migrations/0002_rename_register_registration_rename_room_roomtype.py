# Generated by Django 4.2.11 on 2024-04-06 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Register',
            new_name='Registration',
        ),
        migrations.RenameModel(
            old_name='Room',
            new_name='RoomType',
        ),
    ]
