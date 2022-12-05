from django.urls import path
from app3.views import *

app_name='bala'
urlpatterns=[
    path('veera/',veera,name='veera')
]