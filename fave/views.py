from rest_framework import generics, permissions
from lastseenapi.permissions import IsOwnerOrReadOnly
from .models import Fave
from .serializers import FaveSerializer


class FaveList(generics.ListCreateAPIView):
    '''
    Users can Fave and view Captions.
    '''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FaveSerializer
    queryset = Fave.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FaveDetail(generics.RetrieveDestroyAPIView):
    '''
    Fave can be retrieved and deleted.
    '''
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FaveSerializer
    queryset = Fave.objects.all()
