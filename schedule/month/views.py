from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from .models import author

# Create your views here.

month_schedule = {
    'january': 'learning python',
    'febuarry':'learning .net',
    'march':None,
    'april':'learning java'
}

def index(request):
    months=list(month_schedule.keys())
    return render(request,'month/index.html',{
        'month':months
    })
def month_in_number(request,month):
    months = list(month_schedule.keys())
    if(month > len(month_schedule)):
        return HttpResponseNotFound('invalid month')
    redirect_month=months[month-1] #january[0]
    redirect_path= reverse('month-detail',args=[redirect_month]) #month/january
    return HttpResponseRedirect(redirect_path)


def montly_details(request,month):
    try:
        month_text = month_schedule[month]
        # response_data=render_to_string('month/month.html')
        response_data=render(request,'month/month.html',
                             {'text':month_text})
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound('<h1>this is not mentioned<h1>')
