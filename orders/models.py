from django.db import models

# Create your models here.



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


class Sub(models.Model):
    SIZE_CHOICES = [
        ('S', 'Small'),
        ('L', 'Large'),
    ]

    size = models.CharField(
        max_length=1,
        choices=SIZE_CHOICES,
        default='S',
    )

    ingrediant = models.CharField(max_length = 64)

    cost = models.DecimalField(max_digits=4, decimal_places=2)


class Pasta(models.Model):
    ingrediant =  models.CharField(max_length = 64)
    cost = models.DecimalField(max_digits=3, decimal_places=2)


class Salad(models.Model):
    ingrediant =  models.CharField(max_length = 64)
    cost = models.DecimalField(max_digits=3, decimal_places=2)

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
