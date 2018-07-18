from django.db import models
from django_countries.fields import CountryField
from django.utils import timezone

# Create your models here.
MARITAL = (
	('single','Single'),
	('married','Married'),
	('widowed','Widowed'),
	('divorced','Divorced'),
)

GENDER = (
	('male','Male'),
	('female','Female'),
)

RELATION = (

	('child','Child'),
	('wife','wife'),
	('husband','husband'),

	)

class Position(models.Model):
	pos_type = models.CharField(max_length=30)
	default_deduction = models.DecimalField(max_digits=10, decimal_places=3)
	main_salary_max = models.DecimalField(max_digits=10, decimal_places=3)
	main_salary_min = models.DecimalField(max_digits=10, decimal_places=3)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.pos_type

	

class Employee(models.Model):
	first_name = models.CharField(max_length=15)
	middle_name = models.CharField(max_length=15)
	last_name = models.CharField(max_length=15)
	nationalID = models.PositiveIntegerField(unique=True)
	job = models.CharField(max_length=50,blank=True , null=True)
	age = models.PositiveIntegerField()
	date_of_birth = models.DateField()
	place_of_birth = CountryField(blank_label='(select country)')
	nationality = CountryField(blank_label='(select country)')
	marital_status = models.CharField(choices=MARITAL,max_length=20)
	gender = models.CharField(choices=GENDER,max_length=10)
	position = models.ForeignKey(Position,on_delete=models.CASCADE)
	phone = models.CharField(max_length=20)
	email = models.EmailField(default='nothing@gmail.com')
	has_siblings = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def full_name(self):
		return "{} {} {}".format(self.first_name,self.middle_name,self.last_name)

	def __str__(self):
		return "{} {}".format(self.first_name,self.last_name) 

	class Meta:
		indexes = [
            models.Index(fields=['first_name',]),
            models.Index(fields=['phone',]),
]

class Sibling(models.Model):
	employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
	relation_type = models.CharField(choices=RELATION, max_length=20 , default='child')
	first_name = models.CharField(max_length=15)
	middle_name = models.CharField(max_length=15)
	last_name = models.CharField(max_length=15)
	age = models.PositiveIntegerField()
	date_of_birth = models.DateField()
	place_of_birth = CountryField(blank_label='(select country)')
	nationality = CountryField(blank_label='(select notionality)')
	gender = models.CharField(choices=GENDER,max_length=10)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "{} {} siblings".format(self.employee.first_name,self.employee.last_name) 

class Salary(models.Model):
	position = models.ForeignKey(Position, on_delete=models.CASCADE)
	employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
	main_salary = models.DecimalField(max_digits=10, decimal_places=3)
	deductions = models.DecimalField(max_digits=10, decimal_places=3)
	earnings = models.DecimalField(max_digits=10, decimal_places=3)
	total_deductions = models.DecimalField(default=0,max_digits=10, decimal_places=3)
	total_salary = models.DecimalField(default=0,max_digits=10, decimal_places=3)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "{} salary".format(self.employee.first_name) 