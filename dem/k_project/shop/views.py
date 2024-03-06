from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,"shop/index.html")
def register(request):
    return render(request,"shop/register.html")
def collection(request):
    Catagory=catagory.objects.filter(status=0)
    return render (request,'shop/collection.html',{"Catagory":Catagory})

def collectionsview(request,name):
    if(catagory.objects.filter(name=name,status=0)):
        products=product.objects.filter(catagory__name=name)
        return render(request,"shop/products/index.html",{"products":products,"catagory_name":name})
    else:
        messages.warning(request,"No Such Catagory Found")
        return redirect('collection')


def prduct_details(request,cname,pname):
    if(catagory.objects.filter(name=cname,status=0)):
        if(product.objects.filter(name=pname,status=0)):
            products=product.objects.filter(name=pname,status=0).first()
            return render(request,"shop/products/product_details.html",{"products":products})
        else:
            messages.error(request,"No Such Catagory Found")
            return redirect('collection')
    else:
        messages.error( request,"No Such Catagory Found")
        return redirect('collection')
