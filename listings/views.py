from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from django.views.generic import View

from .choices import *

from .models import Listings


class ListingsView(ListView):
    queryset = Listings.objects.order_by(
        '-list_date').filter(is_published=True)
    paginate_by = 3
    template_name_suffix = ''
    context_object_name = 'listings'

class ListingDetail(View):
    template = 'listings/listing.html'

    def photoList(self, listings):
        internal_photos = []
        for i in range(1, 6):
            if getattr(listings, 'photo_%d' % i):
                photo = getattr(listings, 'photo_%d' % i)
                internal_photos.append(photo)
        return internal_photos

    def get(self, request, listing_id):
        listing = get_object_or_404(Listings, pk=listing_id)
        context = {
            'listing': listing,
            'internal_photos': self.photoList(listing)
        }
        return render(request, self.template, context)


def search(request):
    queryset_list = Listings.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(
                city__iexact=city)

    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(
                state__iexact=state)

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(
                bedrooms__lte=bedrooms)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(
                price__lte=price)

    context = {
        'listings': queryset_list,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'values': request.GET
    }

    return render(request, 'listings/search.html', context)
