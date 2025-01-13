from django.db import models

class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Заказ от {self.first_name} {self.last_name}, Данные: {self.email}, {self.address}, {self.city}'


class PositionOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f'Позиция заказа {self.order}'


