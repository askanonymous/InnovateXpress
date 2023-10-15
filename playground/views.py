from django.shortcuts import render 
from django. http import HttpResponse

def say_hello(request):
    # return HttpResponse ('Hello World')
    return render(request,'hello.html',{'name':'akshit'})

def no_results(request):
    return render(request,'results.html')
def mean(request):
    return render(request,'results.html')
def median(request):
    return render(request,'results.html')