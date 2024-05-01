# Generated by Django 4.2.11 on 2024-04-20 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_alter_registration_notes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membership', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='registration',
            name='membership',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='book.membership'),
            preserve_default=False,
        ),
    ]
