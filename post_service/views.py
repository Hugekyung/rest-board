from django.views.generic import ListView

from post_service.models import Post


class PostListView(ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'post_service/post_list.html'
    paginate_by = 5