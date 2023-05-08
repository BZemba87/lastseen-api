from rest_framework import generics, permissions, filters
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from .models import Caption
from .serializers import CaptionSerializer
from lastseenapi.permissions import IsOwnerOrReadOnly


class CaptionList(generics.ListCreateAPIView):
    """
    List all captions
    Create a caption
    Perform_create method associates caption with logged in user
    """
    serializer_class = CaptionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Caption.objects.annotate(
        comments_count=Count('comment', distinct=True),
        fave_count=Count('fave', distinct=True)
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'love__owner__profile',
        'owner__profile',
        'fave__owner__profile',
    ]
    search_fields = [
        'owner__username',
        'title',
    ]
    ordering_fields = [
        'comments_count',
        'love__created_at',
        'fave__created_on',
        'fave_count',
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
    queryset = Caption.objects.annotate(
        comments_count=Count('comment', distinct=True),
        love_count=Count('love', distinct=True),
        fave_count=Count('fave', distinct=True)
    ).order_by('-created_at')
