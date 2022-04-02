from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.contrib import admin
# from rest_framework import permissions
#
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

# schema_view = get_schema_view(
#    openapi.Info(
#       title="Documentación de API",
#       default_version='v0.1',
#       description="API de Reserva de Habitaciónes con DRF",
#       terms_of_service="",
#       contact=openapi.Contact(email="ebrjose@gmail.com"),
#       license=openapi.License(name="BSD License"),
#    ),
#    public=True,
#    permission_classes=(permissions.AllowAny,),
# )

urlpatterns = [
   # re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

   path('admin/', admin.site.urls),
    path('', include(('users.urls', 'users'), namespace='users')),   
   path('rooms/', include('src.rooms.routers')),
   # path('api/reservations/', include('src.reservations.api.routers')),
   # path('api/payments/', include('src.payments.api.routers')),
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)