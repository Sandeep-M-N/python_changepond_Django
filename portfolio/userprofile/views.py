from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Portfolio,feedback
from .forms import ProjectFieldform,Feedbackform
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
# Create your views here.
def index(request):
    
    post=Portfolio.objects.all().order_by("-id")[0:3]
    # Handle the feedback form
    if request.method == 'POST':
        form=Feedbackform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thankyou')
    else:
        form=Feedbackform()
    return render(request,'userprofile/index.html',{
        'post':post,
        'form':form
    })
def allpost(request):
    post=Portfolio.objects.all()
    return render(request,'userprofile/allpost.html',{
        'post':post
    })
def post_detail(request,postdetail):
    full_details=Portfolio.objects.get(slug=postdetail)
    return render(request,'userprofile/Description.html',{
        'read':full_details,
    })
def thankyou(request):
    return render(request,'userprofile/thankyou.html')

class ProjectsubmitCreateView(CreateView):
   model=Portfolio
   form_class=ProjectFieldform
   template_name="userprofile/forms.html"
   success_url="adminupload"


# class FeedbacksubmitView(CreateView):
#     model=feedback
#     form_class=Feedbackform
#     template_name='userprofile/index.html'
#     success_url="/thankyou"