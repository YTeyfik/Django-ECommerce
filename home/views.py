from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from Produce.models import Category, Produce
from home.models import Setting, ContactFormu, ContactFormMessage


def index(request):
    setting=Setting.objects.get(pk=1)
    sliderdata=Produce.objects.all()[:5]
    dayproducts=Produce.objects.all()[:4]
    lastproducts = Produce.objects.all().order_by('-id')[:4]
    randomproducts = Produce.objects.all().order_by('?')[:4]
    category=Category.objects.all()
    context={'setting':setting,'page':'home',
             'sliderdata':sliderdata,'category':category
             ,'dayproducts':dayproducts,'lastproducts':lastproducts
             ,'randomproducts':randomproducts}
    return render(request,'index.html',context)

def about(request):
    setting=Setting.objects.get(pk=1)
    category = Category.objects.all()
    context={'seting':setting,'category':category}
    return render(request,'about.html',context)

def contact(request):
    if request.method=='POST':
        form=ContactFormu(request.POST)
        if form.is_valid():
            data=ContactFormMessage()
            data.name=form.cleaned_data['name']
            data.email=form.cleaned_data['email']
            data.subject=form.cleaned_data['subject']
            data.message=form.cleaned_data['message']
            data.ip=request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request,"Mesajınız başarı ile gönderilmiştir.Teşekkür Ederiz")
            return  HttpResponseRedirect('/contact')

    setting= Setting.objects.get(pk=1)
    category = Category.objects.all()
    form=ContactFormu()
    context={'setting':setting,'form':form,'category': category}
    return render(request, 'contact.html', context)


def category_produces(request,id,slug):
    produces=Produce.objects.filter(category_id=id)
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    context={'produces':produces,'category':category
             ,'categorydata':categorydata}
    return render(request,'produces.html',context)