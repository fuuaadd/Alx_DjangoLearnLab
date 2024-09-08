from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from django.contrib import admin
from django.urls import path, include


router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]