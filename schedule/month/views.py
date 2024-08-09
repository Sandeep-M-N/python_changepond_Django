from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

# Create your views here.

month_schedule = {
    'january': 'learning python',
    'febuarry':'learning .net',
    'march':'learning git',
    'april':'learning java'
}
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
        return HttpResponse(month_text)
    except:
        return HttpResponseNotFound('this is not mentioned')
