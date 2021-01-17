from django.urls import path

from mysite.post_service import views



urlpatterns = [
    path('', views.post_list, name='post_list'),
]
