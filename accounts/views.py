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
        password1 = request.POST.get('pass1')
        password2 = request.POST.get('pass2')
        email = request.POST.get('email')

        # Валидация
        if password1 != password2:
            data['color1'] = 'red'
            data['report1'] = 'Пароли не совпадают'
        # Остальная Валидация
        #
        else:
            data['login'] = username1
            data['pass1'] = password1
            data['pass2'] = password2
            data['email'] = email

            # Добавление пользователя
            username1 = User.objects.create_user(username1, email, password1)
            username1.save()

        data['title'] = 'Отчёт о регистрации'

        if username1 is None:
            data['color1'] = 'red'
            data['report1'] = 'В регистрация отказанно'
        else:
            data['color1'] = 'green'
            data['report1'] = 'Регистрация завершина'
    return render(request, 'accounts/report.html', context=data)


def report(request):
    data = {'title': 'Результат регистрации'}
    return render(request, 'accounts/report.html', context=data)


def sign_in(request):
    data = dict()
    if request.method == 'GET':
        data['title'] = 'Авторизация'
        return render(request, 'accounts/sign_in.html', context=data)
    elif request.method == 'POST':
        username1 = request.POST.get('login')
        password1 = request.POST.get('pass1')
        user = authenticate(request, username=username1, password=password1)

        if user is None:
            data['color1'] = 'red'
            data['report1'] = 'Вы не зарегистрированы'
            data['title'] = 'Отчёт об авторизации'
            return render(request, 'accounts/report.html', context=data)
        else:
            login(request, user)
            return redirect('/')


def logout1(request):
    logout(request)
    return redirect('/')


def profile(request):
    data = {'title': 'Профиль пользователя'}
    return render(request, 'accounts/report.html', context=data)


def ajax_reg(request):
    response = dict()
    login_y = request.GET.get('login')

    try:
        User.objects.get(username=login_y)
        response['message'] = 'Логин занят'
    except User.DoesNotExist:
        response['message'] = 'Логин свободен'
    return JsonResponse(response)


