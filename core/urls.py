from django.urls import path, include
from . import views

urlpatterns = [
    path("products/", views.list_product, name="list-product"),
    path("products/<int:id>", views.get_product, name="get-product"),
    path("collections/", views.list_collection, name="list-collection"),
]
