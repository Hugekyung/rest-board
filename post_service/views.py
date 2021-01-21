from django.contrib.auth.views import LoginView
from django.views.generic import ListView
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer


class PostListView(ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'post_service/post_list.html'


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('title')
    serializer_class = PostSerializer