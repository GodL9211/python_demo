from django.conf import settings
from django.conf.urls import url
from django.urls import path, re_path, include
from django.views.generic import RedirectView
from django.views.static import serve
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Blog System API",
        description="Blog site",
        default_version='v1',
        terms_of_service="",
        contact=openapi.Contact(email="zgj0607@163.com"),
        license=openapi.License(name="GPLv3 License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include('blog.urls', namespace='blog')),
    path('', include('common.urls', namespace='common')),
    url(r'^favicon.ico$', RedirectView.as_view(url=r'static/img/favicon.ico')),
    url(r'upload/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(
        r"api/swagger(?P<format>\.json|\.yaml)",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("docs/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
