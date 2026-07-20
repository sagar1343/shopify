from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


router.register("collections", views.CollectionViewset)
router.register("products", views.ProductViewset)

urlpatterns = router.urls
