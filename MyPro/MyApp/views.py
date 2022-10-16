from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect


# Create your views here.

def myfun(request):
	return HttpResponse("welcom to my Pro")

def facebook(request):
	return HttpResponseRedirect("https://www.facebook.com/")

def load_html(request):
	return render (request,'my.html')






