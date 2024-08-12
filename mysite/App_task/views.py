from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect

# Create your views here.

def page_redirect(request,link):
    if (link=='changepond'):
        return HttpResponseRedirect('https://www.changepond.com/')
    elif(link=='accenture'):
        return HttpResponseRedirect('https://www.accenture.com/in-en')
    elif(link=='zoho'):
        return HttpResponseRedirect('https://www.zoho.com/')
    else:
        return HttpResponse("link not found")
    
