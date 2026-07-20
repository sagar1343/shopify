from rest_framework import serializers
from .models import Product, Collection


class CollectionSerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Collection
        fields = ["id", "title", "product_count"]

    def get_product_count(self, collection):
        return collection.products.count()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "collection",
            "description",
            "inventory",
            "price",
            "created_at",
            "updated_at",
        ]
