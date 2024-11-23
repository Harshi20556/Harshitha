from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Harshitha(request):
    return HttpResponse('my name is harshitha')
def Pranay(request):
    return HttpResponse('<h1> <marquee>my sir </marquee></h1>')
def nandu(request):
    return HttpResponse('''
    <h1> name is nandu</h1>
    <i> age is 22</i>
    <b> gender is female</b>
    <img src="https://wallpapercave.com/wp/wp2863036.jpg">
    ''')