# Generated by Django 2.0.5 on 2018-06-20 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SolarDB', '0020_remove_leaseproperty_daterelease'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesproperty',
            name='paidstatus',
            field=models.FloatField(default=None),
        ),
    ]
