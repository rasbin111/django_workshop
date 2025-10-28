from rest_framework import viewsets

from ..models import Post
from .serializers import PostSerializer
from rest_framework.decorators import action


class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(methods=["post"], detail=True)
    def like_post(self, request, pk):
        post = self.get_object()
        
