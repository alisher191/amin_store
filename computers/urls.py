from django.urls import path

from . import views

urlpatterns = [

    path('product-list/', views.ProductList.as_view(), name='products-list'),
    path('product-create/', views.ProductCreate.as_view(), name='add-product'),
    path('product-<int:pk>/', views.ProductReUpDelete.as_view(), name='deleteUpdate-product'),

    path('computers-list/', views.ComputerListView.as_view(), name='computers-list'),
    path('computers-create/', views.ComputerCreate.as_view(), name='add-computer'),
    path('computers-<int:pk>/', views.ComputerReUpDelete.as_view(), name='deleteUpdate-computer'),
]
