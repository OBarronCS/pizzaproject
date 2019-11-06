from django.contrib import admin

from .models import *

# Register your models here.
class ToppingAdmin(admin.ModelAdmin):
    filter_horizontal = ('pizzas',)




admin.site.register(Pizza)
admin.site.register(Topping, ToppingAdmin)
admin.site.register(Pasta)
admin.site.register(Sub)
admin.site.register(SubMainTopping)
admin.site.register(SubSubTopping)
admin.site.register(Salad)
admin.site.register(Platter)
