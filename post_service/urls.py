from django.urls import path, include

from .views import PostListView, LoginView


app_name = 'post_service'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('login/', LoginView.as_view(template_name='post_service/login.html'), name='login'),
    # path('login/validate', views.login_validate)
]
