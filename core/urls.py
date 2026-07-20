from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.ProductList.as_view(), name="list-product"),
    path("products/<int:pk>", views.ProductDetails.as_view(), name="product-details"),
    path("collections/", views.CollectionList.as_view(), name="list-collection"),
    path(
        "collections/<int:pk>",
        views.CollectionDetails.as_view(),
        name="collection-details",
    ),
]
