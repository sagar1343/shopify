from rest_framework import serializers
from .models import Product, Collection


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ["id", "title", "created_at", "updated_at"]


class ProductSerializer(serializers.ModelSerializer):
    collection = CollectionSerializer()

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "collection",
            "description",
            "price",
            "created_at",
            "updated_at",
        ]
