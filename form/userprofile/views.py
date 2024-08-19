from django.shortcuts import render
from django.http import HttpResponseRedirect
from.forms import feedbackform

# Create your views here.
def index(request):
    if request.method == 'POST': 
        # enter_username=request.POST['username']
        # if enter_username=="":
        #     return render(request,'userprofile/forms.html',{
        #         'haserror':True
        #     })
        form=feedbackform(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('thankyou')
    form=feedbackform()
    return render(request,'userprofile/forms.html',{
        'form':form
    })

def thankyou(request):
    return render(request,'userprofile/thank_you.html')