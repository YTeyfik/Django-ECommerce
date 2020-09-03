
from django.urls import include,path
from.import views

urlpatterns=[
    path('',views.index,name='index'),
    path('addtocart/<int:id>',views.addtocart,name='addtocart'),
    path('deletefromcart/<int:id>',views.deletefromcart,name='deletefromcart')
]