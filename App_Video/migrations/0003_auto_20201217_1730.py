# Generated by Django 3.1.3 on 2020-12-17 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Video', '0002_auto_20201217_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.CharField(max_length=264),
        ),
    ]
