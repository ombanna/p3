from django.shortcuts import render, HttpResponse
from .models import Restaurant, Food, Order
from math import ceil


def index(request):
    allproducts = []
    catproducts = Restaurant.objects.values('category')
    cats = {item['category'] for item in catproducts}
    for cat in cats:
        prod = Restaurant.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allproducts.append([prod, range(1, nSlides), nSlides])
    params = {'allproducts': allproducts}
    return render(request, 'restaurant/index.html', params)


def restaurant(request, myid):
    restaurant = Restaurant.objects.filter(id=myid)
    food = Food.objects.filter(restaurant_id=myid)
    return render(request, 'restaurant/restaurantview.html', {'restaurant': restaurant[0], 'food': food})


def detail(request, myid):
    if request.method == "POST":
        item_id = myid
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        order = Order(name=name, phone=phone, item_id=item_id)
        order.save()
        thank = True
        return render(request, 'restaurant/detail.html', {'item_id': item_id, 'thank': thank})
    return render(request, 'restaurant/detail.html')


def forgotpassword(request):
    return render(request, 'restaurant/forgot-password.html')


def login(request):
    return render(request, 'restaurant/login.html')


def register(request):
    return render(request, 'restaurant/register.html')


def report(request):
    orders = Order.objects.all()
    return render(request, 'restaurant/report.html', {'orders': orders})


def invoice(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        try:
            order = Order.objects.filter(order_id=orderId)
            if len(order) > 0:
                return HttpResponse(request, 'restaurant/invoice.html')
            else:
                return HttpResponse('{"status": "NoItems"}')
        except Exception as e:
            return HttpResponse('{"status": "Error"}')
    return render(request, 'restaurant/invoice.html')
