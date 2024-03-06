from django.http import JsonResponse
from django.shortcuts import render,redirect
from shop.form import CustomUserForm
from . models import*
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import json
from django.views import generic
from django.core.mail import send_mail
# Create your views here.

def home(request):
    products=product.objects.filter(trending=1)
    return render(request,"shop/inder.html",{"products":products})

def remove_cart(request,cid):
    cartitem=Cart.objects.get(id=cid)
    cartitem.delete()
    return redirect("/cart")

def cart_page(request):
    if request.user.is_authenticated:
        cart=Cart.objects.filter(User=request.user)
        return render(request,"shop/cart.html",{"cart":cart})
    else:
        return redirect("/")

def add_to_cart(request):
    if request.headers.get('X-Requested-With')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            product_qty=data['product_qty']
            product_id=data['pid']
            #print(request.user.id)
            product_status=product.objects.get(id=product_id)
            if product_status:
                if Cart.objects.filter(User=request.user.id,product_id=product_id):
                    return JsonResponse({'status':'Product Already in cart'},status=200)
                else:
                    if product_status.quantity>=product_qty:
                        Cart.objects.create(User=request.user,product_id=product_id,product_qty=product_qty)
                        return JsonResponse({'status':'Product Added to cart'},status=200)
                    else:
                        return JsonResponse({'status':'Product Stock Not Available'},status=200)
        else:
            return JsonResponse({'status':'Login to add cart'},status=200)
    else:
        return JsonResponse({'status':'Invalid Access'},status=200)

def remove_fav(request,cid):
    cartitem=Favourite.objects.get(id=cid)
    
    cartitem.delete()
    return redirect("/fav")

def fav_page(request):
    if request.user.is_authenticated:
        favourite=Favourite.objects.filter(User=request.user)
        return render(request,"shop/fav.html",{"favourite":favourite})
    else:
        return redirect("/")
     
def favourite_page(request):
    if request.headers.get('X-Requested-With')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            product_id=data['pid']
            product_status=product.objects.get(id=product_id)
            if product_status:
                if Favourite.objects.filter(User=request.user.id,product_id=product_id):
                    return JsonResponse({'status':'Product Already in Favorite'},status=200)
                else:
                    Favourite.objects.create(User=request.user,product_id=product_id)
                    return JsonResponse({'status':'Product Added to Favorite'},status=200)
        else:
            return JsonResponse({'status':'Login to Add Favorite'},status=200)
    else:
        return JsonResponse({'status':'Invalid Access'},status=200)

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged out Successfully")
    return redirect('/')

def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            User=authenticate(request,username=name,password=pwd)
            if User is not None:
                login(request,User)
                messages.success(request,"Logged in Successfully")
                return redirect("/")
            else:
                messages.error(request,"Invalid User Name or Password")
                return redirect('/login')
        return render(request,"shop/login.html")

def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registeration Success You can Login Now ...!")
            return redirect('/login')
    return render(request,'shop/register.html',{"form":form})

def collection(request):
    Catagory=catagory.objects.filter(status=0)
    return render(request,'shop/collection.html',{"Catagory":Catagory})

def collectionview(request,name):
    if(catagory.objects.filter(name=name,status=0)):
        products=product.objects.filter(catagory__name=name)
        return render(request,"shop/products/inder.html",{"products":products,"catagory_name":name})
    else:
       
        return redirect('collection')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        body=request.POST.get('body')
        print(name,email,body)
        send_mail(
            'Caddcentre - Chat',
            name +" - " +body,
            email,
            ['sarathi202003@gmail.com'],
            fail_silently=False,
        )
    return render(request,"shop/contact.html")

class about(generic.ListView):
    model = catagory
    template_name="shop/about.html"

def product_details(request,cname,pname):
    if(catagory.objects.filter(name=cname,status=0)):
        if(product.objects.filter(name=pname,status=0)):
            products=product.objects.filter(name=pname,status=0).first()
            return render(request,'shop/products/product_details.html',{"products":products})
        else:
            messages.error(request,"No Such Catagory Found")
            return redirect('collection')
    else:
         messages.error(request,"No Such Catagory Found")   
         return redirect('collection')        
        