from django.urls import path
from . import views


urlpatterns = [
    path("adminupload",views.ProjectsubmitCreateView.as_view()),
    path("index",views.index),
    path('submit-feedback', views.FeedbacksubmitView.as_view(), name='submit_feedback'),
    path("thankyou",views.thankyou),
    path("allpost",views.allpost,name='allpost-detail'),
    path("<str:postdetail>",views.post_detail,name='post-description'),
    

]
