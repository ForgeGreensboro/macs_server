# Generated by Django 2.0.1 on 2018-02-01 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('macs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='member_name',
            field=models.TextField(default=''),
        ),
    ]
