from .views import ExternalTeamRegistrationViewSet, InternalTeamRegistrationViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'internalReg', InternalTeamRegistrationViewSet, base_name='internal')
router.register(r'externalReg', ExternalTeamRegistrationViewSet, base_name='external')

urlpatterns = router.urls
