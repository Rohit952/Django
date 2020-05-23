from django.shortcuts import render
import datetime

# Create your views here.

def template_view(request):
    dt = datetime.datetime.now()
    name = 'rohit'
    rolno = 100
    marks = 100
    my_dict = {'date' : dt,'name' : name, 'marks' : marks, 'rollno' : rolno}
    return render(request,'TestApp2/results.html',context = my_dict)
    # return render(request,'TestApp2/results.html', {'date' : dt})

def wish(request):
    date = datetime.datetime.now()
    h = int(date.strftime('%H'))
    msg = 'Hello Guest !! Very Good'
    if h < 12:
        msg = msg + ' Morning'
    elif h < 16:
        msg = msg + ' Afternoon'
    elif h < 21:
        msg = msg + ' Evening'
    else:
        msg = msg + ' Night'
    return render(request, 'TestApp2/results1.html', {'m':msg, 'date':date})


