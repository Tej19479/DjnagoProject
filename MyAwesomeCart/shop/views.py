import json
from math import ceil
from django.http import HttpResponse
from .paytm import Checksum
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Product, Contact, Orders, OrderUpdate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

MERCHANT_KEY = "bKMfNxPPf_QdZppa"


@login_required(login_url='login')
def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)


def searchMatch(query, item):
    '''return true only if query matches the item'''
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False


def search(request):
    query = request.GET.get('search')
    print(query)
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]

        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, "msg": ""}
    if len(allProds) == 0 or len(query) < 4:
        params = {'msg': "Please make sure to enter relevant search query"}
    return render(request, 'shop/search.html', params)


def about(request):
    return render(request, 'shop/about.html')


def logout(request):
    return redirect('LoginPage')


def contact(request):
    if request.method == "POST":
        print(request)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        print(name, email, phone, desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')


def productView(request):
    return render(request, 'shop/prodView.html')


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        print("Total Price of the amount ", amount)

        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city, state=state,
                       zip_code=zip_code, phone=phone, amount=amount)
        order.save()
        thank = True
        id = order.order_id
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        # return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})
        # Request to paytm to transfer the amount to your account  after payment by user

        param_dict = {

            'MID': 'WorldP64425807474247',
            'ORDER_ID': str(order.order_id),
            'TXN_AMOUNT': str(amount),
            'CUST_ID': email,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'PAYTM_MOBILE ': str(phone),
            'CALLBACK_URL': 'http://127.0.0.1:8000/shop/handlerequest'

        }
        param_dict['CHECKSUMHASH'] = Checksum.verify_checksum(param_dict, MERCHANT_KEY)
        print("param dict", param_dict)
        return render(request, 'shop/paytm.html', {'param_dict': param_dict})
    return render(request, 'shop/checkout.html')


@csrf_exempt
def handlerequest(request):
    form = request.POST
    print("from value is", form)
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
    if i == 'CHECKSUMHASH':
        checksum = response_dict[i]

        verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
        if verify:
            if response_dict['RESPCODE'] == '01':
                print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'shop/paymentstatus.html', {'response': response_dict})


def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        print(orderId, email)
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            print(order)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderId)

                updates = []

                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].items_json], default=str)

                return HttpResponse(response)

            else:
                return HttpResponse('else')

        except Exception as e:
            return HttpResponse('Exception')

    return render(request, 'shop/tracker.html')


def SignupPage(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        print(uname, email, pass1, pass2)
        my_user = User.objects.create_user(uname, email, pass1)
        my_user.first_name = fname
        my_user.last_name = lname
        my_user.save()
        messages.sucess(request, "Your account has been successfully")
        return redirect('LoginPage')
        return HttpResponse("suceesfull")
    return render(request, 'shop/signup.html')
