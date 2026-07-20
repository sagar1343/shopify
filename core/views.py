from .models import Product, Collection
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import (
    WriteProductSerializer,
    ReadProductSerializer,
    CollectionSerializer,
)
from rest_framework import status

# Create your views here.


@api_view(["GET", "POST"])
def list_product(request):
    if request.method == "GET":
        queryset = Product.objects.all()
        serializer = ReadProductSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = WriteProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def get_product(request, id):
    instance = get_object_or_404(Product, id=id)
    if request.method == "GET":
        serializer = ReadProductSerializer(instance)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = WriteProductSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "PATCH":
        serializer = WriteProductSerializer(
            data=request.data, instance=instance, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(["GET", "POST"])
def list_collection(request):
    if request.method == "GET":
        queryset = Collection.objects.all()
        serializer = CollectionSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = CollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def get_collection(request, id):
    instance = get_object_or_404(Collection, pk=id)
    if request.method == "GET":
        serializer = CollectionSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = CollectionSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PATCH":
        serializer = CollectionSerializer(
            data=request.data, instance=instance, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
