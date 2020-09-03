from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from Produce.models import Category
from order.models import ShopCartForm, ShopCart


def index(request):
    return HttpResponse("order app")

@login_required(login_url='/login')
def addtocart(request,id):
    url=request.META.get('HTTP_REFERER')
    current_user = request.user

    scart=ShopCart.objects.filter(produce_id=id)
    if scart:
        control=1
    else:
        control = 0


    if request.method=='POST': #ürün formdan geldiyse
        form=ShopCartForm(request.POST)
        if form.is_valid():
            if control==1:
                data=ShopCart.objects.get(produce_id=id)
                data.quantity+= form.cleaned_data['quantity']
                data.save()
            else:
                data=ShopCart()
                data.user_id=current_user.id
                data.produce_id=id
                data.quantity=form.cleaned_data['quantity']
                data.save()
        messages.success(request,"Ürün sepete eklendi")
        return HttpResponseRedirect(url)
    else:#ürün direk eklendiyse
        if control == 1:
            data = ShopCart.objects.get(produce_id=id)
            data.quantity += 1
            data.save()
        else:
            data=ShopCart()
            data.user_id=current_user.id
            data.produce_id=id
            data.quantity=1
            data.save()
            messages.success(request,"Ürün sepete eklendi")
            return HttpResponseRedirect(url)

    messages.warning(request,"Ürün eklemede hata oluştu")
    return HttpResponseRedirect(url)

@login_required(login_url='/login')
def shopcart(request):
    category=Category.objects.all()
    current_user=request.user
    shopcart=ShopCart.objects.filter(user_id=current_user.id)
    total=0
    for rs in shopcart:
        total+= rs.produce.cost*rs.quantity
    context={
        'shopcart':shopcart,'category':category,
        'total':total,
    }
    return render(request, 'ShopCart_products.html', context)

@login_required(login_url='/login')
def deletefromcart(request,id):
    ShopCart.objects.filter(id=id).delete()
    messages.success(request,"Ürün sepetten silindi")
    return HttpResponseRedirect("/shopcart")