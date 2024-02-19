from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass

@admin.register(CostAnalysis)
class CostAnalysisAdmin(admin.ModelAdmin):
    pass


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    pass