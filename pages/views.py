from django.shortcuts import render
from django.views.generic.list import ListView

from listings.models import Listings, Realtor
from listings.choices import *


class ListingsMainView(ListView):
    queryset = listings = Listings.objects.order_by(
        '-list_date').filter(is_published=True)[:3]
    template_name = 'pages\index.html'
    context_object_name = 'listings'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['state_choices'] = state_choices
        context['bedroom_choices'] = bedroom_choices
        context['price_choices'] = price_choices
        return context


class AboutView(ListView):
    model = Realtor
    queryset = model.objects.order_by('-hire_date')
    template_name = 'pages\/about.html'
    context_object_name = 'realtors'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mvp_realtors'] = Realtor.objects.filter(is_mvp=True)
        return context
