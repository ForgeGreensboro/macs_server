# Generated by Django 2.0.1 on 2018-02-27 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('macs', '0006_auto_20180219_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='members',
            field=models.ManyToManyField(related_name='machines', through='macs.MemberPermission', to='macs.Member'),
        ),
    ]
