# Generated by Django 2.0.1 on 2018-03-07 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('macs', '0010_auto_20180227_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invalidrequest',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='machinelock',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='machineunlock',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
