from django.urls import path
from .import views,models
urlpatterns = [
    path('index',views.index),
    # path('',views.index),
    path('<int:month>', views.month_in_number),  #1
    path('<str:month>', views.montly_details, name='month-detail')
]

# <placeholder> also known as angle bracket