from django.urls import path

from . import views

urlpatterns = [
    path('accessories-list/', views.AccessoriesList.as_view()),
    path('accessories-create/', views.AccesoriesCreate.as_view()),
    path('accessories-<int:pk>/', views.AccessoriesReUpDelete.as_view()),

    path('brands-list/', views.BrandsList.as_view()),
    path('brands-create/', views.BrandCreate.as_view()),
    path('brands-<int:pk>/', views.BrandReUpDelete.as_view()),
]
