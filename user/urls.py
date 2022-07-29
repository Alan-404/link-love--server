from django.urls import path
from user import views
urlpatterns = [
    path('user_api', views.user_api),
    path('auth', views.auth),
    path('image', views.show_image_user),
    path('user_handle', views.user_handle)
]