from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.utils.crypto import get_random_string

from Produce.models import Category, Produce
from home.models import UserProfile
from order.models import ShopCartForm, ShopCart, Order, OrderForm, OrderProduce


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
        request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()
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
    request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()
    messages.warning(request,"Ürün eklemede hata oluştu")
    return HttpResponseRedirect(url)

@login_required(login_url='/login')
def shopcart(request):
    category=Category.objects.all()
    current_user=request.user
    shopcart=ShopCart.objects.filter(user_id=current_user.id)
    request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()

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
    current_user = request.user
    request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()
    messages.success(request,"Ürün sepetten silindi")
    return HttpResponseRedirect("/shopcart")


@login_required(login_url='/login')
def orderproduce(request):
    category=Category.objects.all()
    current_user = request.user
    shopcartt=ShopCart.objects.filter(user_id=current_user.id)
    total=0
    for rs in shopcartt:
        total+=rs.produce.cost*rs.quantity

    if request.method=='POST':
        form=OrderForm(request.POST)

        if form.is_valid():
            data=Order()
            data.first_name=form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.address = form.cleaned_data['address']
            data.city = form.cleaned_data['city']
            data.phone = form.cleaned_data['phone']
            data.user_id = current_user.id
            data.total = total
            data.ip = request.META.get('REMOTE_ADDR')
            ordercode = get_random_string(5).upper()
            data.code=ordercode
            data.save()


            shopcartt=ShopCart.objects.filter(user_id=current_user.id)
            for rs in shopcartt:
                detail=OrderProduce()
                detail.order_id=data.id
                detail.produce_id=rs.produce_id
                detail.user_id=current_user.id
                detail.quantity=rs.quantity

                produce=Produce.objects.get(id=rs.produce_id)
                produce.Quantity -= rs.quantity
                produce.save()

                detail.cost = rs.produce.cost
                detail.amount=rs.amount
                detail.save()


            ShopCart.objects.filter(user_id=current_user.id).delete()
            request.session['cart_items']=0
            messages.success(request,"Your order has been completed")
            return  render(request,'order_completed.html',{'ordercode':ordercode,'category':category})
        else:
            messages.warning(request,form.errors)
            return HttpResponseRedirect("/order/orderproduce")

    form=OrderForm()
    profile=UserProfile.objects.get(user_id=current_user.id)
    context={'shopcartt':shopcartt,
             'category':category,
             'total':total,
             'form':form,
             'profile':profile,
             }
    return render(request,'Order_Form.html',context)