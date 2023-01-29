from rest_framework import generics, permissions
from lastseenapi.permissions import IsOwnerOrReadOnly
from likes.models import Like
from likes.serializers import LikeSerializer


class LikeList(generics.ListCreateAPIView):
    """
    Lists likes and logged in users can create likes
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()


class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    Owner can retrieve or delete like by ID
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
    