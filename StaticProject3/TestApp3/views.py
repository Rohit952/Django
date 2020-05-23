from django.shortcuts import render
import datetime
# Create your views here.

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
    return render(request, 'TestApp3/results3.html', {'m':msg, 'date':date})
