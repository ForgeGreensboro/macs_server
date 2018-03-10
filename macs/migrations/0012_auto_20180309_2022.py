# Generated by Django 2.0.1 on 2018-03-09 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('macs', '0011_auto_20180307_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='machines', to='macs.Location'),
        ),
    ]
