from django.urls import path
from . import views
urlpatterns = [
    path("index",views.index,name='index-detail'),
    path("thankyou",views.thankyou),
]
