from django.urls import path
from . import views

urlpatterns =[
    path('itreg/',views.t_int_reg),
    path('handvrequest/',views.handel_verification_request),
]