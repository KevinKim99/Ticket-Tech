from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("todos/", views.todos, name="Todos"),
    path("concerts/", views.concerts_view, name="concerts"),
    path("login/", views.login_view, name="login"),
    path("Details/", views.Details_view, name="Details"),
    path("cart/", views.cart_view, name="cart"),
    path("search-form/", views.searchform_view, name="search-form"),
    path("search-results/", views.search_results_view, name="search-results"),
    path("signup/", views.signup_view, name="signup"),
    path("userPage/", views.userPage_view, name="userPage"),
    path("artists/", views.artists, name="Artists"),
    path("get_artists/", views.get_artists, name="get_artists"),
    path("get_concerts/", views.get_concerts, name="get_concerts"),
    path("get_client/", views.get_client, name="get_client"),
    path("concerts/Details.html/cart.html/", views.cart_view, name="cart"),
    path("concerts/Details.html/", views.Details_view, name="Details"),
    path('artist/details/<str:artist_name>/', views.artist_details_view, name='artist-details'),
    path("logout/", views.logout_view, name="logout"),  # Moved logout URL pattern here
    path("get_payment/", views.get_payment, name="get_payment")
]

