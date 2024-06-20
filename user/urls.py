from django.urls import path
from .views import signup_view,login_view,logout_page,profile_page

urlpatterns=[
    path('signup/',signup_view,name='royxatdan_o'),
    path('profile/',profile_page,name='profil'),
    path('login/',login_view,name='login_sahifa'),
    path('logout/',logout_page,name='logout_sahifa'),

]

