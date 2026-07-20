from .models import Product, Collection
from django.shortcuts import get_object_or_404
from django.db.models import Count
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import (
    WriteProductSerializer,
    ReadProductSerializer,
    CollectionSerializer,
)
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
# CBV


class ProductList(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        serializer = ReadProductSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = WriteProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductDetails(APIView):
    def get_object(self, id):
        return get_object_or_404(Product, id=id)

    def get(self, request, id):
        instance = self.get_object(id)
        serializer = ReadProductSerializer(instance)
        return Response(serializer.data)

    def put(self, request, id):
        instance = self.get_object(id)
        serializer = WriteProductSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, id):
        instance = self.get_object(id)
        serializer = WriteProductSerializer(
            data=request.data, instance=instance, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        instance = self.get_object(id)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CollectionList(APIView):
    def get(self, request):
        queryset = Collection.objects.all()
        serializer = CollectionSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CollectionDetails(APIView):
    def get(self, request, id):
        instance = get_object_or_404(Collection, pk=id)
        serializer = CollectionSerializer(instance)
        return Response(serializer.data)

    def put(self, request, id):
        instance = get_object_or_404(Collection, pk=id)
        serializer = CollectionSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def patch(self, request, id):
        instance = get_object_or_404(Collection, pk=id)
        serializer = CollectionSerializer(
            data=request.data, instance=instance, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, id):
        instance = get_object_or_404(Collection, pk=id)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
