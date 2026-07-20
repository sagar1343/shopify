from .models import Product, Collection
from .serializers import (
    ProductSerializer,
    CollectionSerializer,
)
from rest_framework.viewsets import ModelViewSet


class ProductViewset(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CollectionViewset(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
