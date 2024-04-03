from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("todos/", views.todos, name="Todos"),
    path('concerts/', views.concerts_view, name = 'concerts'),
    path('login/', views.login_view, name = 'login'),
    path('Details/', views.Details_view, name = 'Details'),
    path('cart/', views.cart_view, name = 'cart'),
    path('search-form/', views.searchform_view, name = 'search-form'),
    path('search-results/', views.searchresults_view, name = 'search-results'),
    path('signup/', views.signup_view, name = 'signup'),
    path('userPage/', views.userPage_view, name = 'userPage'),
    path("artists/", views.artists, name = "Artists"),
    path('get_artists/', views.get_artists, name='get_artists'),
    path('get_client/', views.get_client, name='get_client'),
    path('get_payment/', views.get_payment, name='get_payment'),
    path('concerts/Details.html/', views.Details_view, name = 'Details')
]


