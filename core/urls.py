from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register("products", views.ProductViewset)
router.register("collections", views.CollectionViewset)

urlpatterns = router.urls
