from django.contrib import admin
from .models import Order, Delivery, Feedback


admin.site.register(Order)
admin.site.register(Delivery)
admin.site.register(Feedback)
