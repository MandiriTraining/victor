from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("Belajar Django Luuur")
    return render(request,'landingpage/index.html')
