from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def something(request):
    return HttpResponse('this is the way of creation')
def nothing(request):
    return HttpResponse('reach the goal')