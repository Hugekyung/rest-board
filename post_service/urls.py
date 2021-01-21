from django.urls import path, include
from rest_framework import routers

from .views import PostListView, LoginView, PostViewSet

app_name = 'post_service'

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('api/', include(router.urls)),
    path('login/', LoginView.as_view(template_name='post_service/login.html'), name='login'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('login/validate', views.login_validate)
]
