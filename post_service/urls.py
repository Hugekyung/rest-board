from django.urls import path
from .views import PostListView



urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    # path('login/', views.login),
    # path('login/validate', views.login_validate)
]
