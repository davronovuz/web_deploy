from .views import homepage,contact_page,detail_new,sport_page,xorij_page,\
    texno_page,mahalliy_page,search_page,addcategory_page,addnew_page
from django.urls import path


urlpatterns=[
    path('',homepage,name='bosh_sahifa'),
    path('contact/',contact_page,name='kontact'),
    path('sport/',sport_page,name='sport'),
    path('xorij/',xorij_page,name='xorij'),
    path('texnologiya/',texno_page,name='texno'),
    path('mahalliy/',mahalliy_page,name='mahalliy'),
    path('search/',search_page,name='qidir'),
    path('new/<slug:slug>/',detail_new,name='detail'),
    path('addcategory/', addcategory_page, name='addcat'),
    path('addnew/', addnew_page, name='add_new'),
]

