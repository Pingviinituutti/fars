# Generated by Django 2.0.3 on 2018-03-15 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='name',
            field=models.TextField(default='Booking'),
        ),
    ]
