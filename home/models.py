from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import ModelForm, TextInput, Textarea
from django.utils.safestring import mark_safe


class Setting(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(blank=True, max_length=100)
    keywords = models.CharField(blank=True, max_length=255)
    description = models.CharField(blank=True, max_length=255)
    company = models.CharField(blank=True, max_length=100)
    address = models.CharField(blank=True, max_length=250)
    phone = models.CharField(blank=True, max_length=100)
    fax = models.CharField(blank=True, max_length=100)
    email = models.CharField(blank=True, max_length=100)
    smtpserver = models.CharField(blank=True, max_length=100)
    smtpemail = models.CharField(blank=True, max_length=100)
    smtppassword = models.CharField(blank=True, max_length=100)
    smtpport = models.CharField(blank=True, max_length=100)
    icon = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(blank=True, max_length=100)
    instagram = models.CharField(blank=True, max_length=100)
    twitter = models.CharField(blank=True, max_length=100)
    aboutus = RichTextUploadingField()
    contact = RichTextUploadingField()
    status = models.CharField(max_length=10, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ContactFormMessage(models.Model):
    STATUS= (
        ('New','New'),
        ('Read','Read'),
        ('Closed', 'Closed'),
    )
    name=models.CharField(blank=True,max_length=20)
    email=models.CharField(blank=True,max_length=50)
    subject=models.CharField(blank=True,max_length=50)
    message=models.CharField(blank=True,max_length=255)
    status=models.CharField(max_length=10,choices=STATUS,default='New')
    ip=models.CharField(blank=True,max_length=20)
    note=models.CharField(blank=True,max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ContactFormu(ModelForm):
    class Meta:
        model=ContactFormMessage
        fields=['name','email','subject','message']
        widgets={
            'name':TextInput(attrs={'class':'input','placeholder':'Name & Surname'}),
            'subject': TextInput(attrs={'class': 'input','placeholder': 'Subject'}),
            'email': TextInput(attrs={'class': 'input','placeholder': 'Email Address'}),
            'message': Textarea(attrs={'class': 'input','placeholder': 'Your Message','rows':'5'}),

        }


class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    phone=models.CharField(blank=True,max_length=20)
    address = models.CharField(blank=True, max_length=150)
    city = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=20)
    image = models.ImageField(blank=True, upload_to='images/users/')

    def __str__(self):
        return self.user.username
    def user_name(self):
        return self.user.first_name +' '+ self.user.last_name

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" height="50"/>')
        else:
            return ""

class UserProfileForm(ModelForm):
    class Meta:
        model=UserProfile
        fields=['phone','address','city','country','image']