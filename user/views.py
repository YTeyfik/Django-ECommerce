from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Produce.models import Category
from home.models import UserProfile


@login_required(login_url='/login')
def index(request):

    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'category': category,
                   'profile': profile,
                   }
    return render(request, 'user_profile.html', context)