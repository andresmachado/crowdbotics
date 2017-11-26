from rest_framework import viewsets, permissions

from main.models import Cat, Dog
from .permissions import IsOwnerOrReadOnly
from .serializers import CatSerializer, DogSerializer


# Create your views here.


class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        qs = self.queryset.filter(owner=self.request.user)
        return qs

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class DogViewSet(BaseViewSet):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()

class CatViewSet(BaseViewSet):
    serializer_class = CatSerializer
    queryset = Cat.objects.all()