from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import *
from project.models import *


def hmpage(request):
    pst=Posts.objects.all()
    ctg=Categories.objects.all()
    return render(request,'homepage.html',{'p':pst,'c':ctg})

def menpage(request):
    return render(request,'men.html')

def womenpage(request):
    return render(request,'women.html')

def kidspage(request):
    return render(request,'kids.html')

def hmlvngpage(request):
    return render(request,'home_living.html')

def beautypage(request):
    return render(request,'beauty.html')

def studiopage(request):
    return render(request,'studio.html')

def sample(request):
    form=Posts(request.POST or None,request.Files or None)
    if form.is_valid():
        form.save()
        return redirect('project/form/')
    return render(request,'sample.html',{'forms':form})

# def bohoo(request):
#     boh=bohoocatg.objects.all()
#     return render(request,'boohooman.html',{'b':boh})


def bohoo(request):
    boh=bohoocatg.objects.all()
    return render(request,'products.html',{'b':boh})

def bohoodetails(request,pk):
    det=Posts.objects.get(id=pk)
    return render(request,'product-detail.html',{'d':det})

def uspopage(request):
    return render(request,'uspolo.html')

def logpage(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('homes')
    return render(request,'login.html')

def shopbag(request):
    item=ShoppingBag.objects.all()
    return render(request,'shoppingbag.html',{'items':item})

def insert_shoppingbagView(request,id):
    if request.method=='POST':
        obj=Posts.objects.get(id=id)
        item=ShoppingBag.objects.create(item=obj)
        return redirect('shpbag')
    
def remove(request,id):
    obj=ShoppingBag.objects.get(id=id)
    obj.delete()
    return redirect('shpbag')

def registration(request):
    form=UserForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        form.save()
        return redirect('lginpg')
    return render(request,"registration.html",{'form':form})

def logoutView(request):
    logout(request)
    return redirect('homes')