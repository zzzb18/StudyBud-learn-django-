from nturl2path import url2pathname
from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('rooms/',views.getRooms),
    path('rooms/<str:pk>/',views.getRoom),
]