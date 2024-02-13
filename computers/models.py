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

    def __str__(self):
        return self.name


class Computer(models.Model):
    name = models.CharField(max_length=255)
    descripton = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    video_card = models.ForeignKey(
        AccessoriesType,
        on_delete=models.DO_NOTHING,
        verbose_name='Видео-карта',
        limit_choices_to={'category': AccessoriesType.VIDEO_CARD},
        related_name='video_card'
    )

    cpu = models.ForeignKey(
        AccessoriesType,
        on_delete=models.DO_NOTHING,
        verbose_name='Процессор',
        limit_choices_to={'category': AccessoriesType.CPU},
        related_name='cpu'
    )

    cooler = models.ForeignKey(
        AccessoriesType,
        on_delete=models.DO_NOTHING,
        verbose_name='Охлаждение',
        limit_choices_to={'category': AccessoriesType.COOLER},
        related_name='cooler'
    )

    ram = models.ForeignKey(
        AccessoriesType,
        on_delete=models.DO_NOTHING,
        verbose_name='Оперативная память',
        limit_choices_to={'category': AccessoriesType.RAM},
        related_name='ram'
    )

    system_board = models.ForeignKey(
        AccessoriesType,
        on_delete=models.DO_NOTHING,
        verbose_name='Материнская плата',
        limit_choices_to={'category': AccessoriesType.SYSTEM_BOARD},
        related_name='system_board'
    )

    hhd = models.ForeignKey(
        AccessoriesType,
        on_delete=models.DO_NOTHING,
        verbose_name='Жёсткий диск',
        limit_choices_to={'category': AccessoriesType.HHD},
        related_name='hhd'
    )

    ssd = models.ForeignKey(
        AccessoriesType,
        on_delete=models.DO_NOTHING,
        verbose_name='Диск SSD',
        limit_choices_to={'category': AccessoriesType.SSD},
        related_name='ssd'
    )

    optical_drive = models.ForeignKey(
        AccessoriesType,
        on_delete=models.DO_NOTHING,
        verbose_name='Оптический привод',
        limit_choices_to={'category': AccessoriesType.OPTICAL_DRIVE},
        related_name='optical_drive'
    )

    psu = models.ForeignKey(
        AccessoriesType,
        on_delete=models.DO_NOTHING,
        verbose_name='Блок питания',
        limit_choices_to={'category': AccessoriesType.PSU},
        related_name='psu'
    )

    body = models.ForeignKey(
        AccessoriesType,
        on_delete=models.DO_NOTHING,
        verbose_name='Корпус',
        limit_choices_to={'category': AccessoriesType.BODY},
        related_name='body'
    )

    os = models.ForeignKey(
        AccessoriesType,
        on_delete=models.DO_NOTHING,
        verbose_name='Система',
        limit_choices_to={'category': AccessoriesType.OS},
        related_name='os'
    )

    def __str__(self):
        return self.name
