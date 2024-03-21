from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("todos/", views.todos, name="Todos"),
    path("concerts/", views.concerts, name = "Concerts"),
    path("artists/", views.artists, name = "Artists")
]

