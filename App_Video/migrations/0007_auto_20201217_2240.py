# Generated by Django 3.1.3 on 2020-12-17 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Video', '0006_auto_20201217_1953'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='commenter',
            new_name='user',
        ),
    ]
