from .models import Product, Collection
from .serializers import (
    WriteProductSerializer,
    ReadProductSerializer,
    CollectionSerializer,
)
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class ProductList(ListCreateAPIView):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return WriteProductSerializer
        return ReadProductSerializer


class CollectionList(ListCreateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class ProductDetails(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ReadProductSerializer
        return WriteProductSerializer


class CollectionDetails(RetrieveUpdateDestroyAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
