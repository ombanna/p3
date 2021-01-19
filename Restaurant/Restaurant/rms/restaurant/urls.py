from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('forgotpassword', views.forgotpassword, name='forgotpassword'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path("restaurant/<int:myid>", views.restaurant, name="restaurantview"),
    path("detail/<int:myid>", views.detail, name="order"),
    path("report", views.report,  name="report"),
    path("invoice", views.invoice,  name="invoice"),
]
