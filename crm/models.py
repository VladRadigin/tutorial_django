from django.db import models

class Order(models.Model):
    # Автоматическая фиксация даты, в момент создания
    order_dt = models.DateField(auto_now=True)
    # Текстовое поле
    order_name = models.CharField(max_length=120)
    order_phone = models.CharField(max_length=120)