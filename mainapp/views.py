from django.shortcuts import redirect, render
from mainapp.models import Catagory, Notification, Product_Add, Sign, order_list
from django.contrib.auth import authenticate, login


# Create your views here.
def index_views(request):
    context={}
    noti = Notification.objects.all()
    context = {'noti' : noti}
    order_lists = order_list.objects.all()
    context = {'noti' : noti,
               'order_list': order_lists}
    return render(request, 'index.html',context)

def accounts_views(request):
    return render(request, 'accounts.html')

def login_views(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')
    return render(request, 'login.html')

def signup_views(request):
    context = {}
    if request.method == 'POST':
        data = request.POST
        signup = Sign.objects.create(
            name=data.get('name'),
            username=data.get('username'),
            email=data.get('email'),
            password=data.get('password')
        ) 
        signup.save()
        context = {'signup': signup}
        return redirect('login')
    return render(request,'signup.html',context)

def product_views(request):
    product_add=Product_Add.objects.all()
    cat=Catagory.objects.all()
    context={'product_add':product_add,
             'cat':cat}
    
    return render(request, 'products.html',context)


def add_index_views(request):
    context = {}
    if request.method == 'POST':
        data = request.POST
        order = data.get('order')
        status = data.get('status')
        operator = data.get('operator')
        location = data.get('location')
        distance = data.get('distance')
        start_date = data.get('start_date')
        est_delivery = data.get('est_delivery')
        order_lists = order_list.objects.create(
            order=order,
            status=status,
            operator=operator,
            location=location,
            distance=distance,
            start_date=start_date,
            est_delivery=est_delivery
        )
        context = {"order_lists": order_lists}
        return redirect('index')
    return render(request, 'add_index.html', context)

def delete_index_views(request,pk):
    order_list.objects.filter(pk=pk).delete()
    return redirect('index')

def edit_index_views(request,pk):
    order_lists = order_list.objects.get(id=pk)
    context = {
        "order_lists" : order_lists
    }
    if request.method == 'POST':
        data = request.POST
        order = data.get('order')
        status = data.get('status')
        operator = data.get('operator')
        location = data.get('location')
        distance = data.get('distance')
        start_date = data.get('start_date')
        est_delivery = data.get('est_delivery')

        order_lists.order = order
        order_lists.status = status
        order_lists.operator = operator
        order_lists.location = location
        order_lists.distance = distance
        order_lists.start_date = start_date
        order_lists.est_delivery = est_delivery
        order_lists.save()
        
        return redirect('index')
    return render(request, 'edit_index.html', context)

def add_product_views(request):
    context = {}
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        sold = data.get('sold')
        stock = data.get('stock')
        expire = data.get('expire')
        product_add = Product_Add.objects.create(
            name=name,
            sold=sold,
            stock=stock,
            expire=expire
        )
        context = {"product_add": product_add}
        
        return redirect('products')
    return render(request, 'add_product.html')

def delete_product_views(request,pk):
    Product_Add.objects.filter(pk=pk).delete()
    return redirect('products')

def cat_views(request):
    context = {}
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        cat = Catagory.objects.create(
            name=name
        )
        context = {"cat": cat}
        return redirect('products')
        
        
    return render(request, 'cat.html', context)

def delete_cat_views(request,pk):
    Catagory.objects.filter(pk=pk).delete()
    return redirect('products')

