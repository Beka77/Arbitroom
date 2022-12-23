from django.urls import path
from .views import index
from django.contrib.auth.views import LogoutView

urlpatterns = [ 
    path('',index,name='index'),
    path('logout/', LogoutView.as_view(next_page = 'index'), name="logout"),
]