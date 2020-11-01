from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.contrib import messages

from .models import Shop, City, Category


class HomeView(ListView):
    template_name = 'main_app/home.html'
    model = City

    def get_queryset(self):
        return City.objects.all()


class ShopListView(ListView):
    template_name = 'main_app/shop_list.html'
    model = Shop

    def get_queryset(self):
        city_name = self.kwargs['city_name']
        category = self.kwargs['category'] # .strip("s") # car on affiche au pluriel dans le lien
        if category == "all":
            return Shop.objects.filter(shop_city__city_name=city_name, validated=True).order_by('shop_name')
        else:
            return Shop.objects.filter(shop_city__city_name=city_name, shop_category__category_name=category, validated=True).order_by('shop_name')

    def get_context_data(self, **kwargs):
        city_name = self.kwargs['city_name']
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of the city name
        context['city_name'] = city_name
        # Add all categories of this town
        context['category'] = Category.objects.filter(shop__shop_city__city_name=city_name).distinct().values_list("category_name")
        context['selected_category'] = self.kwargs['category']
        return context


class ShopDetailView(DetailView):
    model = Shop
    template_name = 'main_app/shop_detail.html'


class ShopCreateView(CreateView):
    model = Shop
    fields = ["shop_name", "shop_website_link", "shop_image", "shop_category", "phone_number", "email", "address", "shop_city", "how_to_order"]

    def form_valid(self, form):
        messages.success(self.request, f'Votre demande a bien été prise en compte. Votre boutique sera mise en ligne après notre validation.')
        return super(ShopCreateView, self).form_valid(form)


class MoreInfoView(TemplateView):
    template_name = 'main_app/more_info.html'