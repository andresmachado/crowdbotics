from rest_framework import routers
from .views import DogViewSet, CatViewSet

router = routers.DefaultRouter(trailing_slash=False)

router.register('dogs', DogViewSet)
router.register('cats', CatViewSet)

urlpatterns = router.urls
