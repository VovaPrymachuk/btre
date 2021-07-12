from django.urls import path

from .views import ListingsMainView, AboutView

urlpatterns = [
  path('', ListingsMainView.as_view(), name='index'),
  path('about', AboutView.as_view(), name='about')
]
