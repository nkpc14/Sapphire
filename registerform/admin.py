from django.contrib import admin
from .models import ExternalTeamRegistration, InternalTeamRegistration

admin.site.register(ExternalTeamRegistration)
admin.site.register(InternalTeamRegistration)
