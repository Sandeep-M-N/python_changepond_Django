from django.urls import path
from . import views
urlpatterns = [
    path("index",views.feedbackformView.as_view()),
    path("thankyou",views.ThankyouView.as_view()),
    path("formlist",views.FeedbackView.as_view()),
]
