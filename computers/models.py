from django.db import models


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
WIFI = 'wifi'
AUDIO_CARD = 'audio_card'
MOUSE = 'mouse'
KEYBOARD = 'keyboard'
DISPLAY = 'display'
HEADSET = 'headset'

ACCESSORY_CATEGORY_CHOICES = [
    (VIDEO_CARD, 'Видео-карта'),
    (CPU, 'Процессор'),
    (COOLER, 'Охлаждение'),
    (RAM, 'Оперативная память'),
    (SYSTEM_BOARD, 'Материнская плата'),
    (HHD, 'Жёсткий диск'),
    (SSD, 'Диск SSD'),
    (OPTICAL_DRIVE, 'DVD привод'),
    (PSU, 'Блок питания'),
    (BODY, 'Корпус'),
    (OS, 'Система'),
    (WIFI, 'WI-FI адаптер'),
    (AUDIO_CARD, 'Звуковая карта'),
    (MOUSE, 'Мышь'),
    (KEYBOARD, 'Клавиатура'),
    (DISPLAY, 'Монитор'),
    (HEADSET, 'Гарнитура'),
]

YES = 'yes'
NO = 'no'

YES_NO_CHOICES = [
    (YES, 'есть'),
    (NO, 'нет'),
]


class Brand(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self) -> str:
        return self.name


class VideoCard(models.Model):
    img = models.ImageField(upload_to='videoCardImages/', null=True, blank=True, verbose_name='Изображение')
    name = models.CharField(max_length=255, verbose_name='Название')
    video_memory = models.CharField(max_length=255, null=True, blank=True)

    brand_name = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    category_name = models.CharField(max_length=200, choices=ACCESSORY_CATEGORY_CHOICES)

    def __str__(self) -> str:
        return self.name


class Cpu(models.Model):
    img = models.ImageField(upload_to='cpuImages/', null=True, blank=True, verbose_name='Изображение')
    name = models.CharField(max_length=255, verbose_name='Название')
    l3_cache_volume = models.CharField(max_length=255, verbose_name='Объем кэша L3')
    socket = models.CharField(max_length=100, blank=True, null=True, verbose_name='Сокет')
    cores_quantity = models.IntegerField(blank=True, null=True, verbose_name='Количество ядер')
    processor_frequency = models.CharField(max_length=200, blank=True, null=True, verbose_name='Частота процессора')
    core = models.CharField(max_length=255, blank=True, null=True, verbose_name='Ядро')
    max_frequency_TB = models.CharField(max_length=255, blank=True, null=True, verbose_name='Максимальная частота с Turbo Boost')

    brand_name = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    category_name = models.CharField(max_length=200, choices=ACCESSORY_CATEGORY_CHOICES)

    def __str__(self) -> str:
        return self.name


class Cooler(models.Model):
    img = models.ImageField(upload_to='coolerImages/', null=True, blank=True, verbose_name='Изображение')
    name = models.CharField(max_length=255, verbose_name='Название')
    radiator_material = models.CharField(max_length=255, verbose_name='Материал радиатора')
    height = models.IntegerField(default=0, verbose_name='Высота кулера')
    heat_pipes = models.IntegerField(default=0, verbose_name='Количество тепловых трубок')
    rotation_speed = models.CharField(max_length=255, verbose_name='Скорость вращения')
    air_flow = models.CharField(max_length=255, verbose_name='Воздушный поток')
    noise_level = models.CharField(max_length=255, verbose_name='Уровень шума')
    type_of_bearing = models.CharField(max_length=255, verbose_name='Тип подшипника')
    backlight = models.CharField(max_length=255, verbose_name='Подсветка')
    work_time = models.CharField(max_length=255, null=True, blank=True, verbose_name='Время безотказной работы')
    weight = models.IntegerField(default=0, verbose_name='Вес')
    water_block_material = models.CharField(max_length=255, null=True, blank=True, verbose_name='Материал водоблока')

    brand_name = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    category_name = models.CharField(max_length=200, choices=ACCESSORY_CATEGORY_CHOICES)

    def __str__(self) -> str:
        return self.name


class Ram(models.Model):
    img = models.ImageField(upload_to='coolerImages/', null=True, blank=True, verbose_name='Изображение')
    name = models.CharField(max_length=255, verbose_name='Название')
    memory_type = models.CharField(max_length=255, verbose_name='Тип памяти')
    volume = models.CharField(max_length=255, verbose_name='Объем')
    radiator = models.CharField(max_length=255, verbose_name='Радиатор')
    form_factor = models.CharField(max_length=255, verbose_name='Форм-фактор')
    frequency = models.IntegerField(default=0, verbose_name='Тактовая частота')
    bandwith = models.CharField(max_length=255, verbose_name='Пропускная способность')
    voltage = models.CharField(max_length=255, verbose_name='Напряжение питания')

    brand_name = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    category_name = models.CharField(max_length=200, choices=ACCESSORY_CATEGORY_CHOICES)

    def __str__(self) -> str:
        return self.name


class Motherboard(models.Model):
    img = models.ImageField(upload_to='motherboardImages/', null=True, blank=True, verbose_name='Изображение')
    name = models.CharField(max_length=255, verbose_name='Название')
    form_factor = models.CharField(max_length=255, verbose_name='Форм-фактор')
    slots = models.IntegerField(default=0, verbose_name='Количество слотов памяти')
    chipset = models.CharField(max_length=255, verbose_name='Чипсет')
    sound = models.CharField(max_length=255, verbose_name='Звук')
    socket = models.CharField(max_length=100, blank=True, null=True, verbose_name='Сокет')
    expansion_slots = models.TextField(blank=True, null=True, verbose_name='Слоты расширения')
    m_2_slots_type = models.TextField(blank=True, null=True, verbose_name='Тип слотов M.2')

    brand_name = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    category_name = models.CharField(max_length=200, choices=ACCESSORY_CATEGORY_CHOICES)

    def __str__(self) -> str:
        return self.name


class Hard(models.Model):
    img = models.ImageField(upload_to='hardDiskImages/', null=True, blank=True, verbose_name='Изображение')
    name = models.CharField(max_length=255, verbose_name='Название')
    hard_type = models.CharField(max_length=255, verbose_name='Тип')
    volume = models.IntegerField(default=0, verbose_name='Объём')
    read_write_speed = models.CharField(max_length=255, verbose_name='Скорость записи/Скорость чтения')
    buffer_volume = models.CharField(max_length=255, verbose_name='Объем буферной памяти')
    connect = models.CharField(max_length=255, verbose_name='Подключение')

    brand_name = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    category_name = models.CharField(max_length=200, choices=ACCESSORY_CATEGORY_CHOICES)

    def __str__(self) -> str:
        return self.name


class Ssd(models.Model):
    img = models.ImageField(upload_to='ssdImages/', null=True, blank=True, verbose_name='Изображение')
    name = models.CharField(max_length=255, verbose_name='Название')
    volume = models.IntegerField(default=0, verbose_name='Ëмкость')
    form_factor = models.CharField(max_length=255, verbose_name='Форм-фактор')
    flash_memory_type = models.CharField(max_length=255, verbose_name='Тип флэш-памяти')
    m2_connector = models.CharField(max_length=255, verbose_name='Разъем M.2', choices=YES_NO_CHOICES)
    max_speed = models.CharField(max_length=255, verbose_name='Макс. скорость интерфейса')
    reading = models.CharField(max_length=255, verbose_name='Скорость чтения')
    recording = models.CharField(max_length=255, verbose_name='Скорость записи')

    brand_name = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    category_name = models.CharField(max_length=200, choices=ACCESSORY_CATEGORY_CHOICES)

    def __str__(self) -> str:
        return self.name


class DVDDrive(models.Model):
    INSIDE = 'inside'
    OUTSIDE = 'outside'

    IN_OUT_CHOICES = [
        (INSIDE, 'Внутренний'),
        (OUTSIDE, 'Внешний'),
    ]

    img = models.ImageField(upload_to='dvdDriveImages/', null=True, blank=True, verbose_name='Изображение')
    name = models.CharField(max_length=255, verbose_name='Название')
    drive_type = models.CharField(max_length=255, verbose_name='Тип привода')
    connection_interface = models.CharField(max_length=255, verbose_name='Интерфейс подключения')
    max_speed = models.CharField(max_length=255, verbose_name='Макс. скорость интерфейса')
    placement = models.CharField(max_length=255, verbose_name='placement', choices=IN_OUT_CHOICES)

    brand_name = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    category_name = models.CharField(max_length=200, choices=ACCESSORY_CATEGORY_CHOICES)

    def __str__(self) -> str:
        return self.name


class PowerUnit(models.Model):
    img = models.ImageField(upload_to='powerUnitImages/', null=True, blank=True, verbose_name='Изображение')
    name = models.CharField(max_length=255, verbose_name='Название')
    power = models.IntegerField(default=0, verbose_name='Мощность')
    standart = models.CharField(max_length=255, verbose_name='Стандарт')

    brand_name = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    category_name = models.CharField(max_length=200, choices=ACCESSORY_CATEGORY_CHOICES)

    def __str__(self) -> str:
        return self.name


class Body(models.Model):
    img = models.ImageField(upload_to='bodyImages/', null=True, blank=True, verbose_name='Изображение')
    name = models.CharField(max_length=255, verbose_name='Название')
    form_factor = models.CharField(max_length=255, verbose_name='Форм-фактор')
    standart_size = models.CharField(max_length=255, verbose_name='Типоразмер')
    liquid_cooler_system_poss = models.CharField(max_length=200, choices=YES_NO_CHOICES, verbose_name='Возможность установки жидкостного охлаждения')
    max_heigh_proccessor_cooler = models.CharField(max_length=255, verbose_name='Максимальная высота процессорного кулера')
    max_video_card_length = models.CharField(max_length=255, verbose_name='Максимальная длина видеокарты')
    dimensions = models.CharField(max_length=255, verbose_name='Габариты (ШхВхГ)')
    front_pannel_connectors = models.TextField(verbose_name='Разъемы на лицевой панели')
    remove_air_filter = models.CharField(max_length=255, verbose_name='Съемный воздушный фильтр', choices=YES_NO_CHOICES)

    brand_name = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    category_name = models.CharField(max_length=200, choices=ACCESSORY_CATEGORY_CHOICES)

    def __str__(self) -> str:
        return self.name


class WiFiAdapter(models.Model):
    img = models.ImageField(upload_to='wifiImages/', null=True, blank=True, verbose_name='Изображение')
    name = models.CharField(max_length=255, verbose_name='Название')
    form_factor = models.CharField(max_length=255, verbose_name='Форм-фактор')
    wireless_standart = models.CharField(max_length=255, verbose_name='Стандарт беспроводной связи')
    external_antennas = models.CharField(max_length=200, verbose_name='Количество внешних антенн')
    info_protection = models.CharField(max_length=255, verbose_name='Защита информации')
    max_wireless_speed = models.CharField(max_length=255, verbose_name='Макс. скорость беспроводного соединения')

    brand_name = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    category_name = models.CharField(max_length=200, choices=ACCESSORY_CATEGORY_CHOICES)

    def __str__(self) -> str:
        return self.name


class AudioCard(models.Model):
    img = models.ImageField(upload_to='audioCardImages/', null=True, blank=True, verbose_name='Изображение')
    name = models.CharField(max_length=255, verbose_name='Название')
    manufacturer = models.CharField(max_length=255, verbose_name='Производитель')
    placement_type = models.CharField(max_length=255, verbose_name='Тип расположения')
    connection_type = models.CharField(max_length=200, verbose_name='Тип подключения')
    multi_channel_audio = models.CharField(max_length=255, verbose_name='Возможность вывода многоканального звука')
    jack_3_5 = models.IntegerField(default=0, verbose_name='Входных разъемов jack 3.5 мм')
    micro_input = models.IntegerField(default=0, verbose_name='Микрофонных входов')

    brand_name = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    category_name = models.CharField(max_length=200, choices=ACCESSORY_CATEGORY_CHOICES)

    def __str__(self) -> str:
        return self.name


class OSystem(models.Model):
    img = models.ImageField(upload_to='ssdImages/', null=True, blank=True, verbose_name='Изображение')
    name = models.CharField(max_length=255, verbose_name='Название')

    brand_name = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    category_name = models.CharField(max_length=200, choices=ACCESSORY_CATEGORY_CHOICES)

    def __str__(self) -> str:
        return self.name


class Mouse(models.Model):
    img = models.ImageField(upload_to='ssdImages/', null=True, blank=True, verbose_name='Изображение')
    name = models.CharField(max_length=255, verbose_name='Название')
    mouse_type = models.CharField(max_length=255, verbose_name='Тип')
    connection_interface = models.CharField(max_length=255, verbose_name='Интерфейс подключения')
    scroll_wheel = models.CharField(max_length=255, verbose_name='Колесо прокрутки', choices=YES_NO_CHOICES)
    keys = models.IntegerField(default=0, verbose_name='Количество клавиш')
    optical_resolution = models.CharField(max_length=255, verbose_name='Разрешение оптического сенсора')
    weight = models.CharField(max_length=255, verbose_name='Вес')
    sensor_resolution = models.CharField(max_length=255, verbose_name='Разрешение сенсора')
    mouse_design = models.CharField(max_length=255, verbose_name='Дизайн мыши')
    manufacturer = models.CharField(max_length=255, verbose_name='Производитель')

    brand_name = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    category_name = models.CharField(max_length=200, choices=ACCESSORY_CATEGORY_CHOICES)

    def __str__(self) -> str:
        return self.name


class Keyboard(models.Model):
    img = models.ImageField(upload_to='ssdImages/', null=True, blank=True, verbose_name='Изображение')
    name = models.CharField(max_length=255, verbose_name='Название')
    equipment = models.CharField(max_length=255, verbose_name='Комплектация')
    appointment = models.CharField(max_length=255, verbose_name='Назначение')
    connection_interface = models.CharField(max_length=255, verbose_name='Интерфейс подключения')
    keyboard_type = models.CharField(max_length=255, verbose_name='Тип')
    digital_block = models.CharField(max_length=255, verbose_name='Цифровой блок', choices=YES_NO_CHOICES)
    key_illumination = models.CharField(max_length=255, verbose_name='Подсветка клавиш', choices=YES_NO_CHOICES)
    keys = models.IntegerField(default=0, verbose_name='Количество клавиш')

    brand_name = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    category_name = models.CharField(max_length=200, choices=ACCESSORY_CATEGORY_CHOICES)

    def __str__(self) -> str:
        return self.name


class Screen(models.Model):
    YESS = 'yes'
    NOO = 'no'
    CHOICES = [
        (YESS, "да"),
        (NOO, "нет")
    ]

    img = models.ImageField(upload_to='ssdImages/', null=True, blank=True, verbose_name='Изображение')
    name = models.CharField(max_length=255, verbose_name='Название')
    diagonal = models.CharField(max_length=255, verbose_name='Диагональ')
    screen_resolution = models.CharField(max_length=255, verbose_name='Разрешение')
    brightness = models.CharField(max_length=255, verbose_name='Яркость')
    contrast = models.CharField(max_length=255, verbose_name='Контрастность')
    response_time = models.CharField(max_length=255, verbose_name='Время отклика')
    max_colors = models.CharField(max_length=255, verbose_name='Максимальное количество цветов')
    update_frequency = models.CharField(max_length=255, verbose_name='Частота обновления')
    height_adjustment = models.CharField(max_length=255, verbose_name='Регулировка по высоте', choices=CHOICES)

    brand_name = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    category_name = models.CharField(max_length=200, choices=ACCESSORY_CATEGORY_CHOICES)

    def __str__(self) -> str:
        return self.name


class Headset(models.Model):
    YEES = 'yes'
    NOU = 'no'

    Y_N_CHOICES = [
        (YEES, "да"),
        (NOU, "нет")
    ]

    img = models.ImageField(upload_to='ssdImages/', null=True, blank=True, verbose_name='Изображение')
    name = models.CharField(max_length=255, verbose_name='Название')
    manufacturer = models.CharField(max_length=255, verbose_name='Производитель')
    headset_type = models.CharField(max_length=255, verbose_name='Тип')
    headphone_design = models.CharField(max_length=255, verbose_name='Конструкция наушников')
    connection_type = models.CharField(max_length=255, verbose_name='Тип подключения')
    acoustic_design = models.CharField(max_length=255, verbose_name='Тип акустического оформления')
    mounting_type = models.CharField(max_length=255, verbose_name='Тип крепления')
    cable_connection = models.CharField(max_length=255, verbose_name='Подключение кабеля')
    connector_interface = models.CharField(max_length=255, verbose_name='Интерфейс/разъём подключения')
    volume_control = models.CharField(max_length=255, verbose_name='Регулятор громкости', choices=Y_N_CHOICES)
    folding_design = models.CharField(max_length=255, verbose_name='Складная конструкция', choices=Y_N_CHOICES)
    color = models.CharField(max_length=255, verbose_name='Цвет')
    weight = models.CharField(max_length=255, verbose_name='Вес')
    guarantee = models.CharField(max_length=255, verbose_name='Гарантия')
    battery_life = models.CharField(max_length=255, verbose_name='Продолжительность работы от аккумуляторов')
    battery_of_battery = models.CharField(max_length=255, verbose_name='Тип элементов питания')
    wireless_connection = models.CharField(max_length=255, verbose_name='Тип беспроводной связи')
    range_of_action = models.CharField(max_length=255, verbose_name='Радиус действия')
    bluetooth_version = models.CharField(max_length=255, verbose_name='Версия Bluetooth')
    case_included = models.CharField(max_length=255, verbose_name='Чехол/футляр в комплекте', choices=Y_N_CHOICES)

    brand_name = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    category_name = models.CharField(max_length=200, choices=ACCESSORY_CATEGORY_CHOICES)

    def __str__(self) -> str:
        return self.name


class Computer(models.Model):
    POWERFUL = 'powerful'
    GAMING = 'gaming'
    CHEAP = 'cheap'

    COMPUTER_CHOICES = [
        (POWERFUL, 'Мощный компьютер'),
        (GAMING, 'Игровой компьютер'),
        (CHEAP, 'Недорогой компьютер')
    ]

    section = models.CharField(max_length=100, choices=COMPUTER_CHOICES, verbose_name='Раздел')
    name = models.CharField(max_length=255, verbose_name='Название компьютера')
    image = models.ImageField(upload_to='computers_picture/', null=True, blank=True, verbose_name='Изображение')
    descripton = models.TextField(verbose_name='Описание компьютера')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    video_card = models.ForeignKey(
        VideoCard,
        on_delete=models.DO_NOTHING,
        verbose_name='Видео-карта',
        limit_choices_to={'category': VideoCard.VIDEO_CARD},
        related_name='video_card'
    )

    cpu = models.ForeignKey(
        Cpu,
        on_delete=models.DO_NOTHING,
        verbose_name='Процессор',
        limit_choices_to={'category': Cpu.CPU},
        related_name='cpu'
    )

    cooler = models.ForeignKey(
        Cooler,
        on_delete=models.DO_NOTHING,
        verbose_name='Охлаждение',
        limit_choices_to={'category': Cooler.COOLER},
        related_name='cooler'
    )

    ram = models.ForeignKey(
        Ram,
        on_delete=models.DO_NOTHING,
        verbose_name='Оперативная память',
        limit_choices_to={'category': Ram.RAM},
        related_name='ram'
    )

    system_board = models.ForeignKey(
        Motherboard,
        on_delete=models.DO_NOTHING,
        verbose_name='Материнская плата',
        limit_choices_to={'category': Motherboard.SYSTEM_BOARD},
        related_name='system_board'
    )

    hhd = models.ForeignKey(
        Hard,
        on_delete=models.DO_NOTHING,
        verbose_name='Жёсткий диск',
        limit_choices_to={'category': Hard.HHD},
        related_name='hhd'
    )

    ssd_1 = models.ForeignKey(
        Ssd,
        on_delete=models.DO_NOTHING,
        verbose_name='Диск SSD 1',
        limit_choices_to={'category': Ssd.SSD},
        related_name='ssd_1',
        null=True,
        blank=True
    )

    ssd_2 = models.ForeignKey(
        Ssd,
        on_delete=models.DO_NOTHING,
        verbose_name='Диск SSD 2',
        limit_choices_to={'category': Ssd.SSD},
        related_name='ssd_2',
        null=True,
        blank=True
    )

    optical_drive = models.ForeignKey(
        DVDDrive,
        on_delete=models.DO_NOTHING,
        verbose_name='Оптический привод',
        limit_choices_to={'category': DVDDrive.OPTICAL_DRIVE},
        related_name='optical_drive'
    )

    psu = models.ForeignKey(
        PowerUnit,
        on_delete=models.DO_NOTHING,
        verbose_name='Блок питания',
        limit_choices_to={'category': PowerUnit.PSU},
        related_name='psu'
    )

    body = models.ForeignKey(
        Body,
        on_delete=models.DO_NOTHING,
        verbose_name='Корпус',
        limit_choices_to={'category': Body.BODY},
        related_name='body'
    )

    os = models.ForeignKey(
        OSystem,
        on_delete=models.DO_NOTHING,
        verbose_name='Система',
        limit_choices_to={'category': OSystem.OS},
        related_name='os'
    )

    wifi = models.ForeignKey(
        WiFiAdapter,
        on_delete=models.DO_NOTHING,
        verbose_name='Система',
        limit_choices_to={'category': WiFiAdapter.WIFI},
        related_name='os'
    )

    audio_card = models.ForeignKey(
        AudioCard,
        on_delete=models.DO_NOTHING,
        verbose_name='Система',
        limit_choices_to={'category': AudioCard.AUDIO_CARD},
        related_name='os'
    )

    def __str__(self):
        return self.name
