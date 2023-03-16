from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def mohana(request):
    return HttpResponse('my name is mohana')
def sample(request):
    return HttpResponse('function name is sample')
def abc(request):
    return HttpResponse('function name is abc')