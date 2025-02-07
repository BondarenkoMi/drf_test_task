from django.urls import path, include
from rest_framework.routers import SimpleRouter
from tasks.views import TaskViewSet
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions



router = SimpleRouter()
router.register(r'tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    path('', include(router.urls), name='tasks'),
    path('users/', include('users.urls')),

]

schema_view = get_schema_view(
    openapi.Info(
        title="Tasks API",
        default_version='v1',
        description="Тестовое задание",
        contact=openapi.Contact(email="email"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]