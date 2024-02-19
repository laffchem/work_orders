from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    address = models.CharField(null=True, max_length=50)
    city = models.CharField(null=True, max_length=50)
    state = models.CharField(null=True, max_length=50)
    zip_code = models.CharField(null=True, max_length=5) # only 5 digit zip.
    work_crew = models.ForeignKey("WorkCrew", on_delete=models.DO_NOTHING)
    

class WorkCrew(models.Model):
    crew_type = models.CharField(max_length=50)


class WorkSheet(models.Model):
    work_date = models.DateTimeField()
    work_crew = models.ForeignKey("WorkCrew", on_delete=models.DO_NOTHING)


