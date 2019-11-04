from registerform.models import ExternalTeamRegistration, InternalTeamRegistration
from .serializers import *
from rest_framework import viewsets


class ExternalTeamRegistrationViewSet(viewsets.ModelViewSet):
    serializer_class = ExternalTeamRegistrationSerializer
    queryset = ExternalTeamRegistration.objects.all()


class InternalTeamRegistrationViewSet(viewsets.ModelViewSet):
    serializer_class = InternalTeamRegistrationSerializer
    queryset = InternalTeamRegistration.objects.all()
