from django.urls import path
from nearbyshops import views

urlpatterns=[
    path('',views.Home.as_view()),
]