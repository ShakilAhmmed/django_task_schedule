
from django.http import HttpResponse
from . import  schedule

def home(request):
    return HttpResponse("Ok")



