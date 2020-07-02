# Generated by Django 2.0.3 on 2018-05-28 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SolarDB', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='leaseProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=255)),
                ('province', models.CharField(max_length=255)),
                ('municipality', models.CharField(max_length=255)),
                ('barangay', models.CharField(max_length=255)),
                ('regLandOwner', models.CharField(max_length=255)),
                ('contactNum', models.CharField(max_length=255)),
                ('Address', models.CharField(max_length=255)),
                ('representative', models.CharField(max_length=255)),
                ('titleNum', models.CharField(max_length=255)),
                ('lotNum', models.CharField(max_length=255)),
                ('areaHectares', models.FloatField(default=None)),
                ('surveyNum', models.CharField(max_length=255)),
                ('pricePerHectare', models.FloatField(default=None)),
                ('totalContractPrice', models.FloatField(default=None)),
                ('firstPayAmount', models.FloatField(default=None)),
                ('firstPayDate', models.DateField(default=None)),
                ('secPayAmount', models.FloatField(default=None)),
                ('secPayDate', models.DateField(default=None)),
                ('thirdPayAmount', models.FloatField(default=None)),
                ('thirdPayDate', models.DateField(default=None)),
                ('fourthPayAmount', models.FloatField(default=None)),
                ('fourthPayDate', models.DateField(default=None)),
                ('fifthPayAmount', models.FloatField(default=None)),
                ('fifthPayDate', models.DateField(default=None)),
                ('sixthPayAmount', models.FloatField(default=None)),
                ('sixthPayDate', models.DateField(default=None)),
                ('seventhPayAmount', models.FloatField(default=None)),
                ('seventhPayDate', models.DateField(default=None)),
                ('eigthPayAmount', models.FloatField(default=None)),
                ('eigthPayDate', models.DateField(default=None)),
                ('ninthPayAmount', models.FloatField(default=None)),
                ('ninthPayDate', models.DateField(default=None)),
                ('tenthPayAmount', models.FloatField(default=None)),
                ('tenthPayDate', models.DateField(default=None)),
                ('releasedPayment', models.FloatField(default=None)),
                ('Payee', models.CharField(max_length=255)),
                ('area', models.FloatField(default=None)),
            ],
        ),
        migrations.DeleteModel(
            name='locationDetail',
        ),
    ]