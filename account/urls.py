from django.urls import path
from account import views
urlpatterns = [
    path('auth', views.auth_account)
]