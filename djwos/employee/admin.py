from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass


@admin.register(WorkCrew)
class WorkCrewAdmin(admin.ModelAdmin):
    pass


@admin.register(WorkSheet)
class WorkSheet(admin.ModelAdmin):
    pass