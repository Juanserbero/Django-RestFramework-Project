from rest_framework.routers import DefaultRouter

from user.viewsets import UserViewSet

router = DefaultRouter()

router.register('', UserViewSet, basename="user")

urlpatterns = router.urls