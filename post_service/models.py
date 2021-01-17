from django.contrib.auth.models import User
from django.db import models



class Post(models.Model):
    title = models.CharField(max_length=1024)
    body = models.CharField(max_length=4096)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # on_delete=models.CASCADE: 게시자가 탈퇴하면 글이 삭제됨
    pub_date = models.DateTimeField(auto_created=True, auto_now_add=True)
