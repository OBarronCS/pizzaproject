from django.contrib import admin

from .models import *

# Register your models here.
class ToppingInline(admin.StackedInline):
    model = Topping.pizzas.through
    extra = 1

class PizzaAdmin(admin.ModelAdmin):
    inlines = [ToppingInline]

class ToppingAdmin(admin.ModelAdmin):
    filter_horizontal = ('pizzas',)


admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Topping, ToppingAdmin)
