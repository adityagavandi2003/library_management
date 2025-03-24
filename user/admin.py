from django.contrib import admin
from user.models import Order
# Register your models here.
@admin.register(Order)
class OrderList(admin.ModelAdmin):
    list_display = ['user','book','order_id','order_created_at']