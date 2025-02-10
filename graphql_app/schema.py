import graphene
from graphene_django.type import DjangoObjectType 
from .models import *

   

class EmployeeType(DjangoObjectType):
    class Meta:
        model = Employee   

class DepartmentType(DjangoObjectType):
    class Meta:
        model = Department

    employees = graphene.List(EmployeeType) 

    def resolve_employees(self):
        return Employee.objects.all()
    

class Query(graphene.ObjectType):
    all_employee = graphene.List(EmployeeType)
    all_department = graphene.List(DepartmentType) 

    employee = graphene.Field(EmployeeType,id=graphene.string())
    department = graphene.Field(DepartmentType,id=graphene.string())

    def resolve_all_employee(slef):
        return Employee.objects.all()
    def resolve_all_department(self):
        return Department.objects.all()
    def resolve_employee(self,id):
        return Employee.objects.get(uuid=id)
    def resolve_department(self,id):
        return Department.objects.get(uuid=id)
class CreateDepartment(graphene.ObjectType):
    class Arguments:
        department_name = graphene.String()
    department = graphene.Field(DepartmentType)

    def mutate(self,info,department_name):
        department = Department(department_name=department_name)
        return CreateDepartment(department=department)    


class CreateEmployee(graphene.ObjectType):
    class Argumnets:
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()
        phone_number = graphene.String()
        department = graphene.UUID()
    employee = graphene.Field(EmployeeType)

    def mutate(self,info,first_name,last_name,email,phone_number,department):
        employee = Employee(first_name=first_name,last_name=last_name,email=email,phone_number=phone_number,department=department)
        employee.save() 
        return CreateEmployee(employee=employee) 
    
class Mutation(graphene.ObjectType):
    create_employee = CreateEmployee.Field()
    create_department = CreateDepartment.Field()   

schema = graphene.Schema(query=Query, mutation=Mutation)
    