from rest_framework import generics, permissions
from lastseenapi.permissions import IsOwnerOrReadOnly
from love.models import Love
from love.serializers import LoveSerializer


class LoveList(generics.ListCreateAPIView):
    """
    Lists loves and logged in users can create love
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LoveSerializer
    queryset = Love.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LoveDetail(generics.RetrieveDestroyAPIView):
    """
    Owner can retrieve or delete like by ID
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LoveSerializer
    queryset = Love.objects.all()
