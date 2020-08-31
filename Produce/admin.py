from django.contrib import admin

# Register your models here.
from mptt.admin import DraggableMPTTAdmin

from Produce.models import Category, Produce, Images, Comment


class ProduceImageInline(admin.TabularInline): #adding image product inline
    model = Images
    extra = 5

class CategoryAdmin(admin.ModelAdmin):
    list_display =['title','status','image_tag']
    list_filter = ['status']
    readonly_fields = ('image_tag',)

class ProduceAdmin(admin.ModelAdmin):
    list_display = ['title','category','cost','image_tag','Quantity','status']
    readonly_fields = ('image_tag',)
    list_filter =['status','category']
    inlines = [ProduceImageInline]


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title','produce','image_tag']
    readonly_fields = ('image_tag',)

class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_produces_count', 'related_produces_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Produce,
                'category',
                'produces_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Produce,
                 'category',
                 'produces_count',
                 cumulative=False)
        return qs

    def related_produces_count(self, instance):
        return instance.produces_count
    related_produces_count.short_description = 'Related produces (for this specific category)'

    def related_produces_cumulative_count(self, instance):
        return instance.produces_cumulative_count
    related_produces_cumulative_count.short_description = 'Related produces (in tree)'

class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject','comment','produce','user','status']
    list_filter = ['status']

admin.site.register(Category,CategoryAdmin2)
admin.site.register(Produce,ProduceAdmin)
admin.site.register(Images,ImagesAdmin)
admin.site.register(Comment,CommentAdmin)