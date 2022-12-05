from django.urls import path
from app1.views import *

app_name='booking'
urlpatterns=[
    path('book/',book,name='book')
]