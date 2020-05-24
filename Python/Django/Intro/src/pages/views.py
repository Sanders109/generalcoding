from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index_view(request, *args, **kwargs):
	return HttpResponse("<h1>Hello World</h1>")

def contact_view(request, *args, **kwargs):
	return HttpResponse("<h1>Contacts Page</h1>")

def about_view(request, *args, **kwargs):
	return HttpResponse("<h1>About Us</h1>")

def social_view(request, *args, **kwargs):
	return HttpResponse("<h1>Social Page</h1>")

