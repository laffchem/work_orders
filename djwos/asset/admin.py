from django.contrib import admin
from .models import Asset, AssetType, MaintenanceItem
# Register your models here.

@admin.register(Asset)
class Asset(admin.ModelAdmin):
    pass


@admin.register(AssetType)
class AssetType(admin.ModelAdmin):
    pass


@admin.register(MaintenanceItem)
class MaintenanceItem(admin.ModelAdmin):
    pass