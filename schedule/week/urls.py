from django.urls import path
from .import views

urlpatterns=[
    path('<int:week>', views.week_in_number),
    path('<str:week>', views.week_details, name='week-detail')
]