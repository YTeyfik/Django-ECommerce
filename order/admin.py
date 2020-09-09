from django.contrib import admin

# Register your models here.
from order.models import ShopCart, Order, OrderProduce


class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['user','produce','cost','quantity','amount']
    list_filter = ['user']

class OrderProduceline(admin.TabularInline):
    model = OrderProduce
    readonly_fields = ('user','produce','cost','quantity','amount')
    can_delete = False
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','phone','city','total','status']
    list_filter = ['status']
    readonly_fields = ('user','address','city','country','phone','first_name','ip','last_name','phone','city','total')
    can_delete = False
    inlines = [OrderProduceline]

class OrderProduceAdmin(admin.ModelAdmin):
    list_display = ['user','produce','cost','quantity','amount']
    list_filter = ['user']




admin.site.register(ShopCart,ShopCartAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderProduce,OrderProduceAdmin)