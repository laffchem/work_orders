# Generated by Django 5.0.2 on 2024-02-19 02:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssetType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('fema_rate', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('function', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MaintenanceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maintenance_item', models.CharField(max_length=50)),
                ('workorders', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_name', models.CharField(max_length=50)),
                ('asset_number', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=255)),
                ('asset_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='asset.assettype')),
            ],
        ),
    ]
