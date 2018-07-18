from django.shortcuts import render,redirect, get_object_or_404
from .models import Employee,Position,Sibling,Salary
# Create your views here.
from .forms import EmployeeForm ,EmployeeFormEdit , SiblingForm , SiblingFormEdit ,SalaryForm , SalaryFormEdit , PositionForm , PositionFormEdit
from django.http import QueryDict


def employee_list(request):
	if request.method == "POST":
		form = EmployeeForm(request.POST or None)
		form.save()
		return redirect('employee_list')	
	all_employee = Employee.objects.all()
	form = EmployeeForm()
	return render(request , 'EmpManager/employee_list.html' ,{'all_employee':all_employee,'form':form})

def siblings_list(request, id):
	this_employee = get_object_or_404(Employee,pk=id)
	all_siblings = Sibling.objects.filter(employee=this_employee)
	if request.method == "POST":
		form = SiblingForm(request.POST or None)
		sibling = form.save(commit=False)
		sibling.employee = this_employee
		sibling.save()
		return redirect('siblings_list' , id)
	form = SiblingForm()
	return render(request , 'EmpManager/siblings_list.html' , {'this_employee':this_employee,'all_siblings':all_siblings,'form':form})

def salarys_list(request, id):
	this_employee = get_object_or_404(Employee,pk=id)
	all_positions = Position.objects.all()
	all_salarys = Salary.objects.filter(employee=this_employee)
	if request.method == "POST":
		form = SalaryForm(request.POST or None)
		salary = form.save(commit=False)
		salary.employee = this_employee
		position_deduction = salary.main_salary*salary.position.default_deduction
		salary.total_deductions = position_deduction + salary.deductions
		salary.total_salary = (salary.main_salary+salary.earnings)-salary.total_deductions
		if (salary.main_salary <= salary.position.main_salary_max) and (salary.main_salary >= salary.position.main_salary_min):
			salary.save()
		return redirect('salarys_list' , id)
	form = SalaryForm()
	return render(request , 'EmpManager/salarys_list.html' , {'this_employee':this_employee,'all_salarys':all_salarys,'form':form,'all_positions':all_positions})


def positions_list(request):
	if request.method == "POST":
		form = PositionForm(request.POST or None)
		form.save()
		return redirect('positions_list')
	all_positions = Position.objects.all()
	form = PositionForm()
	return render(request,'EmpManager/positions_list.html' , {'all_positions':all_positions,'form':form})


def employee_delete(request,id):
	this_employee = get_object_or_404(Employee, pk=id)
	this_employee.delete()
	return redirect('employee_list')


def sibling_delete(request,id):
	this_sibling = get_object_or_404(Sibling , pk=id)
	employee_id = this_sibling.employee.id
	this_sibling.delete()
	return redirect('siblings_list', employee_id)

def salary_delete(request,id):
	this_salary = get_object_or_404(Salary , pk = id)
	employee_id = this_salary.employee.id
	this_salary.delete()
	return redirect('salarys_list' , employee_id)

def position_delete(request , id):
	position = get_object_or_404(Position , pk = id)
	position.delete()
	return redirect('positions_list')

def employee_edit(request , id):
	employee = get_object_or_404(Employee, pk=id)
	form = EmployeeFormEdit(request.POST or None , instance=employee)
	if request.method == 'POST':
		form.save()
		return redirect('employee_list')
	return render(request , 'EmpManager/employee_edit.html' ,{'form':form,'employee':employee})


def sibling_edit(request , id):
	sibling = get_object_or_404(Sibling, pk=id)
	employee = sibling.employee.id
	form = SiblingFormEdit(request.POST or None , instance=sibling)
	if request.method == 'POST':
		form.save()
		return redirect('siblings_list' , employee)
	return render(request , 'EmpManager/sibling_edit.html' ,{'form':form,'sibling':sibling,'employee':employee})


def salary_edit(request , id):
	salary = get_object_or_404(Salary, pk=id)
	employee = salary.employee
	form = SalaryFormEdit(request.POST or None , instance=salary)
	if request.method == "POST":
		form = SalaryForm(request.POST or None , instance=salary)
		salary = form.save(commit=False)
		salary.employee = employee
		position_deduction = salary.main_salary*salary.position.default_deduction
		salary.total_deductions = position_deduction + salary.deductions
		salary.total_salary = (salary.main_salary+salary.earnings)-salary.total_deductions
		if (salary.main_salary <= salary.position.main_salary_max) and (salary.main_salary >= salary.position.main_salary_min):
			salary.save()
		return redirect('salarys_list' , employee.id)
	return render(request , 'EmpManager/salary_edit.html' ,{'form':form,'salary':salary,'employee':employee.id})


def position_edit(request , id):
	position = get_object_or_404(Position , pk=id)
	form = PositionFormEdit(request.POST or None , instance=position)
	if request.method == "POST":
		form.save()
		return redirect('positions_list')
	return render(request , 'EmpManager/position_edit.html' , {'position':position,'form':form})