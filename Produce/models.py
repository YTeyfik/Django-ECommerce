from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe


class Category(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=30)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True) #metin olarak çağırır
    parent =models.ForeignKey('self', blank=True, null=True, related_name='children',on_delete=models.CASCADE)  # cascade silinirken tüm alt kategorileride silmeye yarar
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return  mark_safe('<img src ="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description='Image'

class Produce(models.Model):
        STATUS = (
            ('True', 'Evet'),
            ('False', 'Hayır'),
        )
        category = models.ForeignKey(Category, on_delete=models.CASCADE)  # category tablosu ile ilişki
        title = models.CharField(blank=True, max_length=100)
        keywords = models.CharField(blank=True, max_length=255)
        description = models.CharField(blank=True, max_length=255)
        image = models.ImageField(blank=True, upload_to='images/')
        cost=models.FloatField()
        Quantity=models.IntegerField()
        detail = models.TextField()
        status = models.CharField(max_length=10, choices=STATUS)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.title

        def image_tag(self):
            return  mark_safe('<img src ="{}" height="50"/>'.format(self.image.url))
        image_tag.short_description='Image'

class Images(models.Model):
    produce=models.ForeignKey(Produce,on_delete=models.CASCADE)
    title=models.CharField(max_length=50,blank=True)
    image=models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

    def image_tag(self):
        return  mark_safe('<img src ="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description='Image'