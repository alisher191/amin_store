from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.AccessoriesList.as_view()),
    path('create/', views.AccesoriesCreate.as_view()),
    path('<int:pk>/', views.AccessoriesReUpDelete.as_view()),
]
