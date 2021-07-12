from django.urls import path

from .views import ListingsView, ListingDetail, search

urlpatterns = [
    path('', ListingsView.as_view(), name='listings'),
    path('<int:listing_id>/', ListingDetail.as_view(), name='listing'),
    path('search/', search, name='search'),
]
