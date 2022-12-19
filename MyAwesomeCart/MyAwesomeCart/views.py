from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.contrib import messages


def home(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        try:
            users = User.objects.get(username=uname)
        except User.DoesNotExist:
            users = ""
        if users.__eq__(uname) or pass1 != pass2:
            return HttpResponse("Fail ...")

        else:
            my_user = User.objects.create_user(username=uname, email=email, password=pass2)
            my_user.first_name = fname
            my_user.last_name = lname
            my_user.save()
            login(request, my_user)
            return redirect('shoppe:ShopHome')

    return render(request, "index.html")


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get("username", None)
        pass1 = request.POST.get("pass", None)
        print(pass1, username)
        if username and pass1:
            user = authenticate(request, username=username, password=pass1)
            if user:
                login(request, user)
                return redirect('shoppe:ShopHome')
            return render(request, "login.html", {"data": "incorrect username and password"})
        else:
            messages.success(request, 'Contact request submitted successfully.')

            # return HttpResponse("Username and password is incorrect")
    return render(request, 'login.html')
