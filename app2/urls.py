from django.urls import path
from app2.views import *
app_name='suriya'
urlpatterns=[
    path('gang/',gang,name='gang')
]