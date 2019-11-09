from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from .forms import SignUpForm
from .models import *

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    context = {
        "user": request.user
    }

    return render(request, "orders/index.html", context)


def add_to_cart(request):
    if request.method == "POST":
        size = request.POST.get('size')
        type = request.POST.get('type')
        topping1 = request.POST.get('topping1')
        topping2 = request.POST.get('topping2')
        topping3 = request.POST.get('topping3')

        print(size)
        print(type)
        print(topping1)
        print(topping2)
        print(topping3)

        # some code on school computer didn't get pushed for some reason :(

        pizza = Pizza(size = size, type = type)

        finalprice = 0.0;
        toppingnum = 0;

        if(topping1 != ""):
            toppingnum += 1

        if(topping2 != ""):
            toppingnum += 1

        if(topping3 != ""):
            toppingnum += 1

        if(type == "R"):
            if(size == "S"):
                if(toppingnum == 0):
                    finalprice = 12.7
                if(toppingnum == 1):
                    finalprice = 13.7
                if(toppingnum == 2):
                    finalprice = 15.2
                if(toppingnum == 3):
                    finalprice = 16.2
            elif(size == "L"):
                if(toppingnum == 0):
                    finalprice = 17.95
                if(toppingnum == 1):
                    finalprice = 19.95
                if(toppingnum == 2):
                    finalprice = 21.95
                if(toppingnum == 3):
                    finalprice = 23.95
        if(type == "S"):
            if(size == "S"):
                if(toppingnum == 0):
                    finalprice = 24.45
                if(toppingnum == 1):
                    finalprice = 26.45
                if(toppingnum == 2):
                    finalprice = 28.45
                if(toppingnum == 3):
                    finalprice = 29.45
            elif(size == "L"):
                if(toppingnum == 0):
                    finalprice = 38.70
                if(toppingnum == 1):
                    finalprice = 40.70
                if(toppingnum == 2):
                    finalprice = 42.70
                if(toppingnum == 3):
                    finalprice = 44.70

        pizza.cost = finalprice;
        pizza.save();

        if(topping1 != ""):
            top1 = Topping.objects.get(name = topping1)
            top1.save()

            pizza.toppings.add(top1)

        if(topping2 != ""):
            top2 = Topping.objects.get(name = topping2)
            top2.save()

            pizza.toppings.add(top2)

        if(topping3 != ""):
            top3 = Topping.objects.get(name = topping3)
            top3.save()

            pizza.toppings.add(top3)

        orderItem = OrderItem(pizza = pizza)
        orderItem.save()

        order = Order(user = request.user, progress = 0)
        order.save()

        order.orders.add(orderItem)

        print(order)

        return JsonResponse({"success" : "true", "orderitem":order.__str__()})


def cart_view(request):
    user = request.user

    context = {
        'user' : user,
        "orders" : Order.objects.filter(user = user)
    }

    print(context)
    return render(request,"orders/cart.html", context)

def shop_view(request):

    context = {
        'pizzatoppings' : Topping.objects.all(),
        'submaintoppings' : SubMainTopping.objects.all(),
        'subsubtoppings' : SubSubTopping.objects.all()
    }

    return render(request, "orders/shop.html", context)

def login_view(request):
    # IF USER IS already logged in, redirect home
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))

    # if this getting the form data,
    if request.method == 'GET':
        return render(request, "orders/login.html")

    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

def register_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        form = SignUpForm()

    return render(request,'orders/register.html', {'form':form})
    #username, password, first name, last name, and email address.
