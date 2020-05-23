from django.contrib import admin
from TestApp4.models import Employee

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin): # to get the data in table form
    list_display = ['id', 'Eno', 'Ename','Esal','Eadd']


admin.site.register(Employee, EmployeeAdmin) # if we open admin console we can see Employee data:: registering our model to the admin interface