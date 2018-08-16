from django.urls import path

from . import views

urlpatterns = [
    path("checkout/", views.UserCheckout, name="checkout"),

]
