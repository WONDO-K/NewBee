"""
URL configuration for NewBee project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg       import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="NewBee : 사회초년생을 위한 금융 꿀 정보!",
        default_version='v_0.0.1',
        description="NewBee-Project API 문서",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="wondok95@naver.com"), # 부가정보
        license=openapi.License(name="Yoon&Ho"),     # 부가정보
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),
    # 이 아랫 부분은 우리가 사용하는 app들의 URL들을 넣습니다.
    path('accounts/', include('accounts.urls')),
    path('articles/', include('articles.urls')),
    path('rates/', include('rates.urls')),
    path('products/', include('products.urls')),
    path('words/', include('words.urls')),
    path('recommens/', include('recommens.urls')),
    path('news/', include('news.urls')),
]
