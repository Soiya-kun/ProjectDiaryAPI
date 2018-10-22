from rest_framework import routers
from .views import DayViewSet

router = routers.DefaultRouter()
router.register(r'days', DayViewSet)
