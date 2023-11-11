from django.urls import path
from .views import HomePageView, PokeneaIndexView, PokeneaShowView


urlpatterns = [
  path('', HomePageView.as_view(), name='home'),
  path('pokeneas/', PokeneaIndexView.as_view(), name='pokeneas'),
  path('pokeneas/<str:pk>', PokeneaShowView.as_view(), name='pokenea_show')
]