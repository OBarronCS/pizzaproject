from django.db import models
from django.contrib.auth.models import User


class Topping(models.Model):
    name = models.CharField(max_length = 64)

    def __str__(self):
        return self.name;

class Pizza(models.Model):
    SIZE_CHOICES = [
        ('S', 'Small'),
        ('L', 'Large'),
    ]

    TYPES_CHOICES = [
        ('R', 'Regular'),
        ('S', 'Sicilian'),
    ]

    size = models.CharField(
        max_length=1,
        choices=SIZE_CHOICES,
        default='S',
    )

    type = models.CharField(
        max_length=1,
        choices=TYPES_CHOICES,
        default='R',
    )

    toppings = models.ManyToManyField(Topping, blank = True, related_name='pizzas')

    cost = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        alltoppings = "";

        for top in self.toppings.all():
            alltoppings += top.__str__() + ', '

        return f"{self.type} Pizza: {alltoppings}";

class SubMainTopping(models.Model):
    name = models.CharField(max_length = 64)

    cost = models.DecimalField(max_digits=4, decimal_places=2)

    SIZE_CHOICES = [
        ('S', 'Small'),
        ('L', 'Large'),
    ]

    size = models.CharField(
        max_length=1,
        choices=SIZE_CHOICES,
        default='S',
    )

    def __str__(self):
        return self.name;

class SubSubTopping(models.Model):
    name = models.CharField(max_length = 64)

    cost = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name;

class Sub(models.Model):
    toppings = models.ManyToManyField(SubMainTopping, blank = True, related_name='sub')
    addedtoppings = models.ManyToManyField(SubSubTopping, blank = True, related_name='sub')

    cost = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        maintoppings = "";

        for top in self.toppings.all():
            maintoppings += top.__str__() + ', '

        subtoppings = "";

        for top in self.addedtoppings.all():
            subtoppings += top.__str__() + ', '

        return f"Sub: {maintoppings} + {subtoppings}";


class Pasta(models.Model):
    ingrediant =  models.CharField(max_length = 64)
    cost = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.ingrediant;


class Salad(models.Model):
    ingrediant =  models.CharField(max_length = 64)
    cost = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.ingrediant;

class Platter(models.Model):

    SIZE_CHOICES = [
        ('S', 'Small'),
        ('L', 'Large'),
    ]

    size = models.CharField(
        max_length=1,
        choices=SIZE_CHOICES,
        default='S',
    )

    ingrediant =  models.CharField(max_length = 64)
    cost = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.ingrediant}, {self.size}";


class OrderItem(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, null = True)
    sub =  models.ForeignKey(Sub, on_delete=models.CASCADE, null = True)
    pasta =  models.ForeignKey(Pasta, on_delete=models.CASCADE, null = True)
    salad =  models.ForeignKey(Salad, on_delete=models.CASCADE, null = True)
    platter =  models.ForeignKey(Platter, on_delete=models.CASCADE, null = True)

    def __str__(self):
        for item in self._meta.get_all_field_names():
            if(item != null):
                return item;

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    orders =  models.ManyToManyField(OrderItem, blank = True, related_name='order')
    progress = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        for item in self.orders.all():
            print(item)
