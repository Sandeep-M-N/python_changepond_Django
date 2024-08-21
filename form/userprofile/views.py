from typing import Any
from django.shortcuts import render
from django.http import HttpResponseRedirect
from.forms import feedbackform
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView

# Create your views here.
class feedbackformView(View):
    def get(self, request):
        form=feedbackform()
        return render(request,'userprofile/forms.html',{
        'form':form
    })
    def post(self,request):
        form=feedbackform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('thankyou')
        return render(request,'userprofile/forms.html',{
        'form':form
    })


# def index(request):


    # if request.method == 'POST': 
        # enter_username=request.POST['username']
        # if enter_username=="":
        #     return render(request,'userprofile/forms.html',{
        #         'haserror':True
        #     })
        # form=feedbackform(request.POST)
        # if form.is_valid():
            # review=Review(
            #     user_name=form.cleaned_data['user_name'],
            #     text=form.cleaned_data['message'],
            #     rating=form.cleaned_data['rating']
            # )
    #         form.save()
    #         print(form.cleaned_data)
    #         return HttpResponseRedirect('thankyou')
    # else:
    #     form=feedbackform()
    # return render(request,'userprofile/forms.html',{
    #     'form':form
    # })

# def thankyou(request):
#     return render(request,'userprofile/thank_you.html')

class ThankyouView(TemplateView):
    template_name = "userprofile/thank_you.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] ="thanks a lot"
        return context
    
class FeedbackView(ListView):
    model = Review
    context_object_name='reviews'
    template_name = "userprofile/feedlist.html"

    
