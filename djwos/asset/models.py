from django.db import models

# Create your models here.
class Asset(models.Model):
    asset_name = models.CharField(max_length=50)
    asset_number = models.CharField(max_length=50)
    location = models.CharField(max_length=255)
    asset_type = models.ForeignKey("AssetType", on_delete=models.DO_NOTHING)


class AssetType(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    rate = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    fema_rate = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    function = models.CharField(max_length=50)


# Note this class is referring to places, not vehicles or equipment
class MaintenanceItem(models.Model):
    maintenance_item = models.CharField(max_length=50)
    workorders = models.CharField(max_length=50)
