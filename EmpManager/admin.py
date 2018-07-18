from django.contrib import admin

# Register your models here.
from .models import Employee,Position,Sibling,Salary

admin.site.register(Employee)
admin.site.register(Position)
admin.site.register(Sibling)
admin.site.register(Salary)