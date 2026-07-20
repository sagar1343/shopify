from django.urls import path, include
from . import views

urlpatterns = [
    path("products/", views.ProductList.as_view(), name="list-product"),
    path("products/<int:id>", views.ProductDetails.as_view(), name="product-details"),
    path("collections/", views.CollectionList.as_view(), name="list-collection"),
    path("collections/<int:id>", views.CollectionDetails, name="collection-details"),
]
