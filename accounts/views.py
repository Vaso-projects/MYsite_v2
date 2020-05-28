from django.shortcuts import render


def sign_up(request):
    data = {'title': 'Страница Регистрации'}
    return render(request, 'accounts/sign_up.html', context=data)


def sign_in(request):
    data = {'title': 'Авторизация'}
    return render(request, 'accounts/sign_in.html', context=data)


def sign_out(request):
    data = {'title': 'Выход'}
    return render(request, 'accounts/sign_out.html', context=data)


