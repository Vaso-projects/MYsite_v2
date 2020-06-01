from django.shortcuts import render, redirect
from hashlib import md5
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse


def sign_up(request):
    data = dict()
    if request.method == 'GET':
        data['title'] = 'Страница Регистрации'
        return render(request, 'accounts/sign_up.html', context=data)
    elif request.method == 'POST':
        # Извлечение данных
        username1 = request.POST.get('login')
        password = request.POST.get('pass1')
        password2 = request.POST.get('pass2')
        email = request.POST.get('email')

        # Валидация
        if password != password2:
            data['color1'] = 'red'
            data['report1'] = 'Пароли не совпадают'
        # Остальная Валидация

        else:
            data['login'] = username1
            data['pass1'] = password
            data['pass2'] = password2
            data['email'] = email
            # Добавление пользователя
            username1 = User.objects.create_user(username1, email, password)
            username1.save()

        data['title'] = 'Отчёт о Регистрации'
        if username1 is None:
            data['color1'] = 'red'
            data['report1'] = 'В регистрация отказанно'
        else:
            data['color1'] = 'green'
            data['report1'] = 'Регистрация завершина'
    return render(request, 'accounts/sign_up_res.html', context=data)


def sign_up_res(request):
    data = {'title': 'Результат регистрации'}
    return render(request, 'accounts/sign_up_res.html', context=data)


def sign_in(request):
    data = {'title': 'Авторизация'}
    return render(request, 'accounts/sign_in.html', context=data)


def sign_out(request):
    data = {'title': 'Выход'}
    return render(request, 'accounts/sign_out.html', context=data)


def ajax_reg(request):
    response = dict()
    login_y = request.GET.get('login')

    try:
        User.objects.get(username=login_y)
        response['message'] = 'Логин занят'
    except User.DoesNotExist:
        response['message'] = 'Логин свободен'
    return JsonResponse(response)


