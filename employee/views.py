from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def employee_list(request):
    return HttpResponse('<h1>DRAKUN CORP</h1>')

def employee_details(request, id=None):
    return HttpResponse('<h1>DRAKUN CORP - DETAIL</h1>')