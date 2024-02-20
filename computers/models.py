from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.TextField()
    brand = models.TextField()
    model = models.TextField()
    category = models.TextField()
    year = models.IntegerField(default=0)
    img = models.ImageField(upload_to='products_picture/', null=True, blank=True)
    powerScale = models.IntegerField(default=0)
    importance = models.IntegerField(default=0)
    sale = models.TextField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Computer(models.Model):
    title = models.CharField(max_length=255)
    descripton = models.TextField()
    price = models.TextField()
    brand = models.TextField()
    model = models.TextField()
    year = models.IntegerField(default=0)
    category = models.TextField()
    image = models.ImageField(upload_to='computers_picture/', null=True, blank=True, verbose_name='Изображение')
    powerScale = models.IntegerField(default=0)
    importance = models.IntegerField(default=0)
    is_game = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    sale = models.IntegerField(default=0)
    cpu = models.ForeignKey(Product, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='cpu')
    cooler = models.ForeignKey(Product, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='cooler')
    motherboard = models.ForeignKey(Product, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='motherboard')
    ram = models.ForeignKey(Product, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='ram')
    videoCard = models.ForeignKey(Product, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='videoCard')
    hdd = models.ForeignKey(Product, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='hdd')
    disk1 = models.ForeignKey(Product, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='disk1')
    disk2 = models.ForeignKey(Product, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='disk2')
    dvd = models.ForeignKey(Product, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='dvd')
    body = models.ForeignKey(Product, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='body')
    powerUnit = models.TextField()
    wifi = models.TextField()
    soundCard = models.ForeignKey(Product, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='soundCard')
    operatingSystem = models.TextField()
    mouse = models.ForeignKey(Product, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='mouse')
    keyboard = models.ForeignKey(Product, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='keyboard')
    monitor = models.ForeignKey(Product, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='monitor')
    headset = models.ForeignKey(Product, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='headset')

    def __str__(self):
        return self.title
