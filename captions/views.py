from rest_framework import generics, permissions, filters
from lastseenapi.permissions import IsOwnerOrReadOnly
from .models import Caption
from .serializers import CaptionSerializer


class CaptionList(generics.ListCreateAPIView):
    """
    List all captions
    Create a caption
    Perform_create method associates caption with logged in user
    """
    serializer_class = CaptionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Caption.objects.all()
    filter_backends = [
        filters.SearchFilter,
    ]
    search_fields = [
        'owner__username',
        'title',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CaptionDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    For caption owner to update and delete caption
    Handles requests for captions that don't exist
    """
    serializer_class = CaptionSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Caption.objects.all()
    