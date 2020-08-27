from django.contrib import admin

# Register your models here.
from Produce.models import Category, Produce, Images


class ProduceImageInline(admin.TabularInline): #adding image product inline
    model = Images
    extra = 5

class CategoryAdmin(admin.ModelAdmin):
    list_display =['title','status']
    list_filter = ['status']


class ProduceAdmin(admin.ModelAdmin):
    list_display = ['title','category','cost','Quantity']
    list_filter =['status','category']
    inlines = [ProduceImageInline]


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title','produce','image']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Produce,ProduceAdmin)
admin.site.register(Images,ImagesAdmin)