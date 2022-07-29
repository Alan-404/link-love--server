from django.urls import path
from post import views
urlpatterns = [
    path('post_api', views.post_api),
    path('media', views.media_view)
]