from django.http import HttpResponse
from django.shortcuts import render
import datetime

def time(request):
    time = datetime.datetime.now()
    return HttpResponse("time")
# def time(request):
#     dt_now = datetime.datetime.now()
#     return HttpResponse(dt_now)
def goodbye(request):
    return HttpResponse("goodbye")

