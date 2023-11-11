from django.urls import path, include
from rest_framework import routers
from api_pokenea import views

router=routers.DefaultRouter()
router.register(r'routes', views.PokeneaViewSet)

urlpatterns = [
    path('',include(router.urls))
]