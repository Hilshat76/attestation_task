from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from network.filters import NetworkNodeFilter
from network.models import NetworkNode, Product
from network.serializers import NetworkNodeSerializer, ProductSerializer
from users.permissions import IsActiveUser


class NetworkNodeViewSet(viewsets.ModelViewSet):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsActiveUser]

    filter_backends = (DjangoFilterBackend,)
    filterset_class = NetworkNodeFilter


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveUser]
