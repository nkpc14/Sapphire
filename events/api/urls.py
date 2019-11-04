from .views import EventSerializerViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'events', EventSerializerViewSet, base_name='events')

urlpatterns = router.urls
