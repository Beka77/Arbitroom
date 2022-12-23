from django.shortcuts import render, redirect
from apps.setting.models import Setting
from apps.users.models import User
from django.http import HttpResponse
from django.contrib.auth import login, authenticate

# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        if 'register' in request.POST:
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            email = request.POST.get('email')
            wallet = request.POST.get('wallet')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')
            if password == password2:
                user = User.objects.create(username = username, first_name = first_name, wallet=wallet, email = email)
                user.set_password(password)
                user.save()
                user = User.objects.get(username = username)
                user = authenticate(username = username, password = password)
                login(request, user)
                return redirect('index'),
            
            else:
                return HttpResponse("Пароли не совпадают")
        if 'login' in request== "POST":
            try:
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = User.objects.get(username = username)
                user = authenticate(username = username, password = password)
                login(request, user)
                return redirect('index')
            except:
                return HttpResponse("Неправильные данные")
    context = {
        'setting' : setting,
    }
    return render(request,'Home/index.html',context)