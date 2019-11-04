from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('event', TemplateView.as_view(template_name='index.html')),
    path('about', TemplateView.as_view(template_name='index.html')),
    path('contactUs', TemplateView.as_view(template_name='index.html')),
    path('reg', TemplateView.as_view(template_name='index.html')),
    path('reg', TemplateView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('registerform.api.urls')),
    path('api/', include('events.api.urls')),
    # path('payment/', include('teamregistrations.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
