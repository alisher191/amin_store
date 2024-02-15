from django.urls import path

from . import views

urlpatterns = [

    path('brands-list/', views.BrandsList.as_view()),
    path('brands-create/', views.BrandCreate.as_view()),
    path('brands-<int:pk>/', views.BrandReUpDelete.as_view()),

    path('computers-list/', views.ComputersList.as_view()),
    path('computers-create/', views.ComputerCreate.as_view()),
    path('computers-<int:pk>/', views.ComputerReUpDelete.as_view()),

    path('videocard-list/', views.VideoCardList.as_view()),
    path('videocard-create/', views.VideoCardCreate.as_view()),
    path('videocard-<int:pk>/', views.VideoCardReUpDelete.as_view()),

    path('cpu-list/', views.CpuCardList.as_view()),
    path('cpu-create/', views.CpuCreate.as_view()),
    path('cpu-<int:pk>/', views.CpuCardReUpDelete.as_view()),

    path('cooler-list/', views.CoolerList.as_view()),
    path('cooler-create/', views.CoolerCreate.as_view()),
    path('cooler-<int:pk>/', views.CoolerReUpDelete.as_view()),

    path('ram-list/', views.RamdList.as_view()),
    path('ram-create/', views.RamCreate.as_view()),
    path('ram-<int:pk>/', views.RamReUpDelete.as_view()),

    path('motherboard-list/', views.MotherboardList.as_view()),
    path('motherboard-create/', views.MotherboardCreate.as_view()),
    path('motherboard-<int:pk>/', views.MotherboardReUpDelete.as_view()),

    path('hard-list/', views.HardList.as_view()),
    path('hard-create/', views.HardCreate.as_view()),
    path('hard-<int:pk>/', views.HardReUpDelete.as_view()),

    path('ssd-list/', views.SsdList.as_view()),
    path('ssd-create/', views.SsdCreate.as_view()),
    path('ssd-<int:pk>/', views.SsdReUpDelete.as_view()),

    path('dvddrive-list/', views.DVDDriveList.as_view()),
    path('dvddrive-create/', views.DVDDriveCreate.as_view()),
    path('dvddrive-<int:pk>/', views.DVDDriveReUpDelete.as_view()),

    path('powerunit-list/', views.PowerUnitList.as_view()),
    path('powerunit-create/', views.PowerUnitCreate.as_view()),
    path('powerunit-<int:pk>/', views.PowerUnitReUpDelete.as_view()),

    path('body-list/', views.BodyList.as_view()),
    path('body-create/', views.BodyCreate.as_view()),
    path('body-<int:pk>/', views.BodyReUpDelete.as_view()),

    path('wifiadapter-list/', views.WiFiAdapterList.as_view()),
    path('wifiadapter-create/', views.WiFiAdapterCreate.as_view()),
    path('wifiadapter-<int:pk>/', views.WiFiAdapterReUpDelete.as_view()),

    path('audiocard-list/', views.AudioCardList.as_view()),
    path('audiocard-create/', views.AudioCardCreate.as_view()),
    path('audiocard-<int:pk>/', views.AudioCardReUpDelete.as_view()),

    path('os-list/', views.OSystemList.as_view()),
    path('os-create/', views.OSystemCreate.as_view()),
    path('os-<int:pk>/', views.OSystemReUpDelete.as_view()),

    path('mouse-list/', views.MouseList.as_view()),
    path('mouse-create/', views.MouseCreate.as_view()),
    path('mouse-<int:pk>/', views.MouseReUpDelete.as_view()),

    path('keyboard-list/', views.KeyboardList.as_view()),
    path('keyboard-create/', views.KeyboardCreate.as_view()),
    path('keyboard-<int:pk>/', views.KeyboardReUpDelete.as_view()),

    path('screen-list/', views.ScreenList.as_view()),
    path('screen-create/', views.ScreenCreate.as_view()),
    path('screen-<int:pk>/', views.ScreenReUpDelete.as_view()),

    path('headset-list/', views.HeadsetList.as_view()),
    path('headset-create/', views.HeadsetCreate.as_view()),
    path('headset-<int:pk>/', views.HeadsetReUpDelete.as_view()),
]
