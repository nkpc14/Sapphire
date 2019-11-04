from rest_framework import serializers
from registerform.models import ExternalTeamRegistration, InternalTeamRegistration


class ExternalTeamRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalTeamRegistration
        fields = '__all__'


class InternalTeamRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternalTeamRegistration
        fields = '__all__'
