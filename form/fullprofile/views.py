from django.shortcuts import render
from .forms import Profileform
from django.views import View
from django.http import HttpResponseRedirect
from .models import Profileupload
from django.views.generic.edit import CreateView
from django.views.generic import ListView
# Create your views here.
# def store_file(file):
#     with open('temp/image.jpg','+wb') as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)
# class CreateProfileView(View):
#     def get(self, request):
#         form = Profileform()
#         return render(request,'fullprofile/userform.html',{
#             'form':form
#         })
    
#     def post(self, request):
#         submittedform = Profileform(request.POST,request.FILES)
#         if submittedform.is_valid():
#             # store_file(request.FILES['userimage'])
#             connect=Profileupload(userimage=request.FILES['userimage'])
#             connect.save()

#             return HttpResponseRedirect('/fullprofile')
#         return render(request,'fullprofile/userform.html',{
#             'form':submittedform
#         })
 
class CreateProfileView(CreateView):
    model = Profileupload
    template_name = "fullprofile/userform.html"
    success_url='/fullprofile'
    fields="__all__"
    labels="choose the file to upload"


class ProfileView(ListView):
      model = Profileupload
      template_name = "fullprofile/renderingimg.html"
      context_object_name='renderingimg'




