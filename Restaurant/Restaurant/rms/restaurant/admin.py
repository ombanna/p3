from django.contrib import admin
from .models import Restaurant, Food, Order


class RestaurantAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Restaurant._meta.fields]


class OrderAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Order._meta.fields]


class FoodAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Food._meta.fields]


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Order, OrderAdmin)
