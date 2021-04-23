from django.forms import ModelForm
from .models import Report

class ReportModelForm(ModelForm):
    class Meta:
        model = Report
        fields = ['body']
    