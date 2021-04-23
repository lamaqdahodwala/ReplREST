from django.shortcuts import render
from .forms import ReportModelForm
# Create your views here.

def index(req):
    if req.method == "POST":
        ... 
    else:
        return render(req, 'reports.html')