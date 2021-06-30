from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .serializers import AnimalSerializer
from .models import Animal
from .permissions import IsRaterOrReadOnly


class AnimalList(ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


class AnimalDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsRaterOrReadOnly,)
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer