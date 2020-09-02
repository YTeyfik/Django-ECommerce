
from django.urls import include,path
from.import views

urlpatterns=[
    path('',views.index,name='index'),
    #path('addcomment/<int:id>',views.addcomment,name='addcomment')
]