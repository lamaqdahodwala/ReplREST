from django.shortcuts import render

# Create your views here.

def index(req):
    return render(req, 'index.html')

def apiendpoints(req):
    return render(req, 'endpoints.html')