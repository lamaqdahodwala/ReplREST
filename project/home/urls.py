from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='views'),
    path('reference', views.apiendpoints, name='endpoints')
]
