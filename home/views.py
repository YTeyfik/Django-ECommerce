from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from Produce.models import Category, Produce, Images, Comment
from home.forms import SearchForm, SignUpForm
from home.models import Setting, ContactFormu, ContactFormMessage
from order.models import ShopCart


def index(request):
    setting=Setting.objects.get(pk=1)
    sliderdata=Produce.objects.all()[:5]
    dayproducts=Produce.objects.all()[:4]
    lastproducts = Produce.objects.all().order_by('-id')[:4]
    randomproducts = Produce.objects.all().order_by('?')[:4]
    category=Category.objects.all()
    current_user = request.user
    request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()
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


def produce_detail(request,id,slug):
    category=Category.objects.all()
    images=Images.objects.filter(produce_id=id)
    produce = Produce.objects.get(pk=id)
    comments=Comment.objects.filter(produce_id=id,status='True')
    context={'category':category,'produce':produce
             ,'images':images,'comments':comments,}
    return render(request,'produce_detail.html',context)


def produce_search(request):
    if request.method=='POST':
        form=SearchForm(request.POST)
        if form.is_valid():
            category=Category.objects.all()
            query=form.cleaned_data['query'] #formdan bilgiyi al
            produces=Produce.objects.filter(title__icontains=query) #select from like query
            context={
                'produces':produces,
                'category':category,
            }
            return render(request,'produces_search.html',context)
    return  HttpResponseRedirect('/')

def logout_view(request):
    logout(request)
    return  HttpResponseRedirect('/')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "Kullanıcı adı yada parola yanlış")
            return HttpResponseRedirect('/login')
    category = Category.objects.all()
    context = {

        'category': category,
    }
    return render(request,'login.html',context)


def signup_view(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=password)
            login(request,user)
            return HttpResponseRedirect('/')

    form=SignUpForm()
    category = Category.objects.all()
    context = {
        'category': category,
        'form':form,
    }
    return render(request,'signup.html',context)
