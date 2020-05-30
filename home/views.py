from django.shortcuts import render


def index(request):
    data = {'title': 'Главная страница'}
    return render(request, 'home/index.html', context=data)


def about(request):
    data = {'title': 'О сайте '}
    return render(request, 'home/about.html', context=data)


def blog(request):
    data = {'title': 'Блог> '}
    return render(request, 'home/blog.html', context=data)


def contact(request):
    data = {'title': 'Контакты '}
    return render(request, 'home/contact.html', context=data)
