# Generated by Django 2.1.dev20171216185936 on 2018-05-01 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0002_ordermodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='maxHeight',
            field=models.FloatField(default=None),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='maxLength',
            field=models.FloatField(default=None),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='maxWidth',
            field=models.FloatField(default=None),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='minHeight',
            field=models.FloatField(default=None),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='minLength',
            field=models.FloatField(default=None),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='minWidth',
            field=models.FloatField(default=None),
        ),
    ]
