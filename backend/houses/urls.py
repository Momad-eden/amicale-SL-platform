from rest_framework.routers import DefaultRouter
from .views import (
    HouseViewSet,
    RoomViewSet,
    AssignmentViewSet,
)

router = DefaultRouter()

router.register("houses", HouseViewSet)
router.register("rooms", RoomViewSet)
router.register("assignments", AssignmentViewSet)

urlpatterns = router.urls