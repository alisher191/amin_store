from django.urls import path

from . import views

urlpatterns = [

    path('orders-list/', views.OrderList.as_view(), name='orders-list'),
    path('order-create/', views.OrderCreaete.as_view(), name='add-order'),
    path('order-<int:pk>/', views.OrderReDelete.as_view(), name='delete-order'),

    path('deliveries-list/', views.DeliveryList.as_view(), name='delivery-list'),
    path('delivery-create/', views.DeliveryCreate.as_view(), name='add-delivery'),
    path('delivery-<int:pk>/', views.DeliveryReDelete.as_view(), name='delete-delivery'),
]
