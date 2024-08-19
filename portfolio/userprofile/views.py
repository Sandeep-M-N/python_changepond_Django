from django.shortcuts import render
from django.http import HttpResponse
from .models import Portfolio
# Create your views here.
def index(request):
    post=Portfolio.objects.all()[0:3]
    return render(request,'userprofile/index.html',{
        'post':post,
    })
def allpost(request):
    post=Portfolio.objects.all()
    return render(request,'userprofile/allpost.html',{
        'post':post
    })
def post_detail(request,postdetail):
    full_details=Portfolio.objects.get(title=postdetail)
    return render(request,'userprofile/Description.html',{
        'read':full_details,
    })