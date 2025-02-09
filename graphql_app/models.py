from django.db import models
import uuid

# Create your models here.

class Department(models.Model):
    uuid = models.UUIDField(unique=True, primary_key=True,default=uuid.uuid4)
    department_name = models.CharField
class Employee(models.Model):
    uuid = models.UUIDField(unique=True, primary_key=True,default=uuid.uuid4)
    first_name = models.CharField()
    last_name = models.CharField()
    phone_number = models.CharField(null=True,blank=True)
    email = models.CharField(null=True,blak=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,related_name='employee_department')
    

