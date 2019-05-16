from django.shortcuts import render,redirect
from .models import Admin_Login,Upload_Product,User_Login,user_Orders,Comments
from django.views.generic import UpdateView

from selenium import webdriver


def loginPage(request):
    return render(request,'login.html')

def showAdmin(request):
    return render(request,'admin.html')



def admin_validation(request):
    name=request.POST.get('a_name')
    password=request.POST.get('a_password')
    if Admin_Login.objects.filter(a_username=name) and Admin_Login.objects.filter(a_password=password):
        mess="Admin Login Successfully......"
        return render(request,'admin_login.html',{"message":mess})
    else:
        mess = "Invalid User name and Passwoed"
        return render(request,'admin.html',{"data":mess})

def upload_Product(request):
    return render(request,"upload_project.html")


def upload_Validate(request):
    product_category = request.POST.get("product")
    product_name = request.POST.get("product_name")
    product_brand = request.POST.get("product_brand")
    product_price = request.POST.get("product_price")
    upload_img = request.FILES["file"]
    print(product_price,product_brand,product_name,product_category,upload_img)
    store=Upload_Product(product_category=product_category,product_name=product_name,product_brand=product_brand,product_price=product_price,upload_image=upload_img)
    store.save()
    print("save")
    return render(request,'upload_project.html',{"data":"Product Uploded successfully...."})


def viewallProducts(request):
    data=Upload_Product.objects.all()
    return render(request,'viewall.html',{"data":data})


def userPage(request):


    return render(request,'user.html')


def u_validate(request):
    username=request.POST.get("u_name")
    password=request.POST.get("u_password")
    if User_Login.objects.filter(email=username) and User_Login.objects.filter(u_password=password):
        mess="User Login Successfully......"
        request.session["name"]=username
        return render(request,'user_login.html',{"message":mess})
    else:
        mess = "Invalid User name and Passwoed"
        return render(request,'user.html',{"data":mess})


def showAllProducts(request):
    data = Upload_Product.objects.all()
    return render(request,'user_viewall.html',{"data":data})


def storeOrders(request,pk=None):
    if pk:
        print(pk)
        num=Upload_Product.objects.filter(id=pk).values('product_price','product_brand','product_name','upload_image')
        print(num)
        for x in num:
            price=x['product_price']
            brand=x['product_brand']
            name=x['product_name']
            image=x['upload_image']
            user_Orders(product_price=price,product_brand=brand,product_name=name,upload_image=image).save()

        print("success....")
        data = Upload_Product.objects.all()
        return render(request,'user_viewall.html',{"data":data})


def myOrders(request):
    data=user_Orders.objects.all()
    return render(request,'user_orders.html',{"data":data})


def postComment(request,pk=None):
    num = user_Orders.objects.filter(id=pk)
    return render(request,'post_comment.html',{"data":num})


def saveComment(request):
    rating=request.POST.get('rate')
    comm=request.POST.get('text')
    print(rating,comm)
    username=request.session["name"]
    print(username)
    email=User_Login.objects.filter(u_username=username).values('email')
    print(email)
    for x in email:
        global email1
        email1=x['email']
    Comments(name=username,rate=rating,comment=comm,email=email1).save()
    data = user_Orders.objects.all()
    return render(request,'user_orders.html',{"data":data})


def uLogout(request):
    del request.session["name"]
    return redirect("/user/")