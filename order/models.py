from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import ModelForm

from Produce.models import Produce


class ShopCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    produce=models.ForeignKey(Produce,on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField()

    def __str__(self):
        return self.produce

    @property
    def amount(self):
        return (self.quantity*self.produce.cost)

    @property
    def cost(self):
        return (self.produce.cost)



class ShopCartForm(ModelForm):
    class Meta:
        model=ShopCart
        fields=['quantity']
