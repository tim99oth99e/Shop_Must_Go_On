from django.urls import path

from .views import HomeView, ShopListView, ShopDetailView, ShopCreateView, MoreInfoView

urlpatterns = [
    path('', HomeView.as_view(), name='main_app-home'),
    path('<str:city_name>/<str:category>/', ShopListView.as_view(), name='shop_list'),
    path('<str:city_name>/shop/<int:pk>/', ShopDetailView.as_view(), name='shop_detail'),
    path('add/', ShopCreateView.as_view(), name='shop_create'),
    path('more-info/', MoreInfoView.as_view(), name='more_info')
]
