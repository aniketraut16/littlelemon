from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('menu_item/<int:item_id>/', views.menu_item, name='menu_item'),
]