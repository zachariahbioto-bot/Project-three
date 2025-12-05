from django.urls import path
from . import views

app_name = "hezora"

urlpatterns = [
    path("", views.index, name="index"),
    path("book/<int:pk>/", views.book_detail, name="book_detail"),
    path("book/<int:pk>/download/", views.download_book, name="download_book"),
    path("cart/add/<int:pk>/", views.add_to_cart, name="add_to_cart"),
    path("cart/", views.cart_view, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
]
