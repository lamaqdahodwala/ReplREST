from django.urls import path
from . import views
urlpatterns = [
    path('user/<str:username>', views.UserView.as_view(), name='user'),
    path("board/<str:boardname>", views.BoardView.as_view(), name='board')
]