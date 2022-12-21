from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, World!")

def hello_name(request, name):
    return HttpResponse(f"Hello, {name}!")

def hello_render(request, name):
    context = {'name': name}
    return render(request, 'hello.html', context)