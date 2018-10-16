# Generated by Django 2.0.3 on 2018-10-01 11:26

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0008_merge_20180918_1417'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookableRepeat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delay', models.IntegerField()),
                ('occurences', models.IntegerField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='booking',
            options={'verbose_name': 'Bokning', 'verbose_name_plural': 'Bokningar'},
        ),
        migrations.AlterField(
            model_name='bookable',
            name='id_str',
            field=models.CharField(max_length=32, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Endast alfanumeriska tecken är tillåtna')]),
        ),
        migrations.AlterField(
            model_name='booking',
            name='comment',
            field=models.CharField(max_length=128, verbose_name='kommentar'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='end',
            field=models.DateTimeField(verbose_name='slut'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start',
            field=models.DateTimeField(verbose_name='start'),
        ),
        migrations.AddField(
            model_name='bookablerepeat',
            name='booking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.Booking'),
        ),
    ]
