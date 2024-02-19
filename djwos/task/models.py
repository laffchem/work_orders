from django.db import models
from asset.models import Asset, MaintenanceItem
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    maintenance_item = models.ForeignKey(MaintenanceItem, on_delete=models.DO_NOTHING)
    materials = models.CharField(max_length=50)
    labor_hours = models.DecimalField(max_digits=5, decimal_places=2)
    asset_used = models.ForeignKey(Asset, on_delete=models.DO_NOTHING)
    area_serviced = models.CharField(max_length=50)
    wo_complete = models.BooleanField(default=True)


class CostAnalysis(models.Model):
    task = models.ForeignKey("Task", on_delete=models.DO_NOTHING)
    maintenance_item = models.CharField(max_length=50)
    labor_costs = models.DecimalField(max_digits=5, decimal_places=2)
    material_costs = models.DecimalField(max_digits=5, decimal_places=2)
    contract = models.ForeignKey("Contract", on_delete=models.DO_NOTHING, null=True)


class Contract(models.Model):
    contractor = models.CharField(max_length=100)
    service = models.CharField(max_length=255)
    maintenance_item = models.ForeignKey(MaintenanceItem, on_delete=models.DO_NOTHING)
    project_budget = models.DecimalField(max_digits=12, decimal_places=2)
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    man_hours = models.DecimalField(max_digits=5, decimal_places=2)
    special_service = models.BooleanField(default=False)
    date_serviced = models.DateTimeField()
    invoice_date = models.DateTimeField(default=timezone.now)

    def create_invoice(self):
        contractor = self.contractor
        maintenance_item = self.maintenance_item
        date_serviced = self.date_serviced
        service = self.service
        rate = self.rate
        hours = self.man_hours

        total_cost = round(rate * hours, 2)
        return contractor, maintenance_item, date_serviced, service, total_cost


