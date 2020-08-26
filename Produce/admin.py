from django.contrib import admin

# Register your models here.
from Produce.models import Category, Produce


class CategoryAdmin(admin.ModelAdmin):
    list_display =['title','status']
    list_filter = ['status']


class ProduceAdmin(admin.ModelAdmin):
    list_display = ['title','category','cost','Quantity']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Produce,ProduceAdmin)