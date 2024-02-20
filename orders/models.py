from django.db import models

from computers.models import Computer


class Order(models.Model):
    city = models.TextField()
    street = models.TextField()
    houseOrComplex = models.TextField()
    homeNumber = models.IntegerField(default=0)
    email = models.TextField()
    phoneNumber = models.TextField()
    fullName = models.TextField()
    willBeDeliveredAt = models.DateTimeField()
    computer = models.ForeignKey(Computer, on_delete=models.DO_NOTHING)
    importance = models.IntegerField()
    active = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.product


class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    status = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.status


class Feedback(models.Model):
    title = models.TextField()
    stars = models.IntegerField(default=0)
    active = models.BooleanField(default=False)
    description = models.TextField()
    img = models.ImageField(upload_to='feedBacks_picture/', null=True, blank=True)

    computer = models.ForeignKey(Computer, on_delete=models.DO_NOTHING, related_name='feedback')

    def __str__(self) -> str:
        return self.title
