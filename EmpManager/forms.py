from django.forms import ModelForm
from .models import Employee,Position,Sibling,Salary


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        exclude = {}

class EmployeeFormEdit(ModelForm):
    class Meta:
        model = Employee
        exclude = {'nationalID'}

class SiblingForm(ModelForm):
    class Meta:
        model = Sibling
        exclude = {'employee'}

class SiblingFormEdit(ModelForm):
    class Meta:
        model = Sibling
        exclude = {'employee'}

class PositionForm(ModelForm):
    class Meta:
        model = Position
        exclude = {}
        
class PositionFormEdit(ModelForm):
    class Meta:
        model = Position
        exclude = {}

class SalaryForm(ModelForm):
    class Meta:
        model = Salary
        exclude = {'employee' , 'total_deductions' , 'total_salary'}

class SalaryFormEdit(ModelForm):
    class Meta:
        model = Salary
        exclude = {'employee' , 'total_deductions' , 'total_salary'}