from django.shortcuts import render, redirect
from hashlib import md5
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def sign_up(request):
    data = dict()
    if request.method == 'GET':
        data['title'] = 'Страница Регистрации'
        return render(request, 'accounts/sign_up.html', context=data)
    elif request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('pass1')
        password2 = request.POST.get('pass2')
        email = request.POST.get('email')



def sign_in(request):
    data = {'title': 'Авторизация'}
    return render(request, 'accounts/sign_in.html', context=data)


def sign_out(request):
    data = {'title': 'Выход'}
    return render(request, 'accounts/sign_out.html', context=data)


