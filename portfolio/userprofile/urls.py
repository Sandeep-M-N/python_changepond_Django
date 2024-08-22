from django.urls import path
from . import views


urlpatterns = [
    path("",views.index),
    path("allpost",views.allpost,name='allpost-detail'),
    path("<str:postdetail>",views.post_detail,name='post-description'),

]
