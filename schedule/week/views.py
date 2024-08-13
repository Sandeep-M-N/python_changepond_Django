from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

# Create your views here.

week_schedule = {
    'sunday':'holiday',
    'monday':'learn python',
    'tuesday':'learn .net',
    'wednesday':'learn java',
    'thursday':'learn react',
    'friday':'learn testing',
    'saturday':'learn angular'
}
def index(request):
    weeks=list(week_schedule.keys())
    return render(request,'week/week.html',{
        'week':weeks
    })

    
def week_in_number(request,week):
    weeks=list(week_schedule.keys())
    if(week>len(weeks)):
        return HttpResponseNotFound('inavlid week')
    redirect_week=weeks[week-1]
    redirect_week_path=reverse('week-detail',args=[redirect_week])
    return HttpResponseRedirect(redirect_week_path)

def week_details(request,week):
    try:
        week_text= week_schedule[week]
        reasponse_week= render(request,'week/week.html',{
            'days':week_schedule
        })
        return HttpResponse(reasponse_week)
    except:
        return HttpResponseNotFound('invalid week')
