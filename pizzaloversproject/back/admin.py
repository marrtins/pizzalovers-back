from django.contrib import admin
from .models import PizzaLover


# Register your models here.


class PizzaLoverAdmin(admin.ModelAdmin):
    pass


admin.site.register(PizzaLover, PizzaLoverAdmin)
