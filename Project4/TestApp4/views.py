from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from TestApp4.models import Employee

# Create your views here.

def employee_info_view(request): # To view employees data in the table form in browser
   employees = Employee.objects.all()
   return render(request,'TestApp4/results4.html',{'employees':employees})
   