from django.db import models

class AccessoriesType(models.Model):
    VIDEO_CARD = 'video_card'
    CPU = 'cpu'
    COOLER = 'cooler'
    RAM = 'ram'
    SYSTEM_BOARD = 'system_board'
    HHD = 'hhd'
    SSD = 'ssd'
    OPTICAL_DRIVE = 'optical_drive'
    PSU = 'psu'
    BODY = 'body'
    OS = 'os'

    ACCESSORY_CHOICES = [
        (VIDEO_CARD, 'Видео-карта'),
        (CPU, 'Процессор'),
        (COOLER, 'Охлаждение'),
        (RAM, 'Оперативная память'),
        (SYSTEM_BOARD, 'Материнская плата'),
        (HHD, 'Жёсткий диск'),
        (SSD, 'Диск SSD'),
        (OPTICAL_DRIVE, 'Оптический привод'),
        (PSU, 'Блок питания'),
        (BODY, 'Корпус'),
        (OS, 'Система'),
    ]

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100, choices=ACCESSORY_CHOICES)
