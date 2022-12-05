from django.shortcuts import render

# Create your views here.
def gang(request):
    return render(request,'gang.html')