# Generated by Django 2.1.dev20171216185936 on 2018-05-01 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0003_auto_20180501_0553'),
    ]

    operations = [
        migrations.CreateModel(
            name='customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerID', models.IntegerField()),
                ('company', models.CharField(max_length=50)),
                ('personOfContact', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='formDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('comments', models.TextField()),
                ('equipName', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('time', models.DateTimeField()),
                ('acctNo', models.IntegerField()),
                ('maxHeight', models.FloatField()),
                ('minHeight', models.FloatField()),
                ('maxLength', models.FloatField()),
                ('minLength', models.FloatField()),
                ('maxWidth', models.FloatField()),
                ('minWidth', models.FloatField()),
                ('volume', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobID', models.IntegerField()),
                ('materialRequested', models.CharField(max_length=50)),
                ('customerID', models.IntegerField()),
                ('maxHeight', models.FloatField()),
                ('specialInstruction', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='laborers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('laborId', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('trainingId', models.IntegerField()),
                ('employeeCategory', models.CharField(max_length=50)),
                ('employeeRate', models.CharField(max_length=50)),
                ('benefits', models.TextField()),
                ('cost', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machineID', models.IntegerField()),
                ('machineModelNumber', models.CharField(max_length=50)),
                ('machineModelYear', models.DateTimeField()),
                ('machinePurchaseDate', models.DateTimeField()),
                ('machineCostOfPurchase', models.FloatField()),
                ('materialID', models.IntegerField()),
                ('trainingID', models.IntegerField()),
                ('machineMaintenancePeriod', models.IntegerField()),
                ('machineMaintenanceDuration', models.IntegerField()),
                ('maintenanceCostPerYear', models.FloatField()),
                ('consumablesCostPerHour', models.FloatField()),
                ('machineName', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='machineStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machineID', models.IntegerField()),
                ('status', models.CharField(max_length=50)),
                ('subStatus', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='materials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materialID', models.IntegerField()),
                ('materialName', models.CharField(max_length=50)),
                ('formFactor', models.CharField(max_length=50)),
                ('costPerUnit', models.FloatField()),
                ('leadTime', models.DateTimeField()),
                ('vendor', models.CharField(max_length=50)),
                ('machine', models.CharField(max_length=50)),
                ('amountOnHand', models.FloatField()),
                ('redBinAmount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='schedulingAndUsage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machineStatus', models.CharField(max_length=50)),
                ('time', models.DateTimeField()),
                ('date', models.DateTimeField()),
                ('laborID', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainingId', models.IntegerField()),
                ('trainingName', models.CharField(max_length=50)),
                ('trainingRequired', models.BooleanField()),
            ],
        ),
    ]
