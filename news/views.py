from django.shortcuts import render,get_object_or_404,redirect
from .models import New,Category
from django.db.models import Q
from .forms import AddCategoryForm,AddNewsForm,AddContacForm
from django.contrib.auth.decorators import login_required

def homepage(request):
    latest_new=New.published.order_by('-id').first()
    latest_news=New.published.order_by('-id')[:5]
    sport_news=New.published.filter(category__name="Sport")
    texno_news=New.published.filter(category__name="Texnologiya")
    mahalliy_news=New.published.filter(category__name="Mahalliy")
    xorij_news=New.published.filter(category__name="Xorij")

    context={
        "latest_new":latest_new,
        "latest_news":latest_news,
        "sport_news":sport_news,
        "texno_news":texno_news,
        "mahalliy_news":mahalliy_news,
        "xorij_news":xorij_news,
    }
    return render(request,"index.html",context)



def contact_page(request):
    form=AddContacForm()
    if request.method=='POST':
        form=AddContacForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kontact')
    context={
        "form":form
    }
    return render(request,"contact.html",context)




def detail_new(request,slug):
    # new=New.published.filter(slug=slug)
    new=get_object_or_404(New,slug=slug)
    context={
        "new":new
    }
    return render(request,"single-page.html",context)


def sport_page(request):
    sport_news = New.published.filter(category__name="Sport")
    context={
        "sport_news":sport_news
    }
    return render(request,"sport.html",context)





def xorij_page(request):
    xorij_news = New.published.filter(category__name="Xorij")
    context={
        "xorij_news":xorij_news
    }
    return render(request,"xorij.html",context)


def texno_page(request):
    texno_news = New.published.filter(category__name="Texnologiya")
    context={
        "texno_news":texno_news
    }
    return render(request,"texno.html",context)


def mahalliy_page(request):
    mahalliy_news = New.published.filter(category__name="Mahalliy")
    context={
        "mahalliy_news":mahalliy_news
    }
    return render(request,"mahalliy.html",context)


def search_page(request):
    query=request.GET.get('q')
    results=[]
    if query:
        results=New.objects.filter(Q(title__icontains=query)|Q(body__icontains=query),status=New.Status.Published)  #samarqand  SamarqanD  SAmarqand

    context={
        "results":results,
        "query":query
    }
    return render(request,"search.html",context)




#Categoriya qo'shish uchun view
def addcategory_page(request):
    form=AddCategoryForm()
    if request.method=='POST':
        form=AddCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bosh_sahifa')
    context={
        "form":form
    }
    return render(request,"add_category.html",context)





def addnew_page(request):
    form=AddNewsForm()
    if request.method=='POST':
        form=AddNewsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bosh_sahifa')
    context={
        "form":form
    }
    return render(request,"addnew.html",context)




