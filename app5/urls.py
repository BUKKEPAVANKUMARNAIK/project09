from django.urls import path
from app5.views import *

app_name='ticket'
urlpatterns=[
    path('tickets/',tickets,name='tickets')
]