from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from TestApp4.models import Employee

# Create your views here.


<<<<<<< HEAD
<<<<<<< HEAD
def employee_info_view(request): # To view employees data in the table form in browser
=======
def employee_info_view(request): # To view employees data in table form in browser
>>>>>>> e7a70893256a6d150762948c91c9249eb8ac51ca
=======
def employee_info_view(request): # To view employees data in table form in browser
>>>>>>> e7a70893256a6d150762948c91c9249eb8ac51ca
   employees = Employee.objects.all()
   return render(request,'TestApp4/results4.html',{'employees':employees})
   