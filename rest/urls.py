from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from main import views as main_views

router = routers.DefaultRouter()
router.register(r'products', main_views.ProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
