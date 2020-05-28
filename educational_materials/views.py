from django.shortcuts import render


def index(request):
    data = {'title': 'Главная страница'}
    return render(request, 'educational_materials/base.html', context=data)


def video(request):
    data = {'title': 'Видео'}
    return render(request, 'educational_materials/video.html', context=data)


def homework(request):
    data = {'title': 'Домашняя работа'}
    return render(request, 'educational_materials/homework.html', context=data)


def presentations(request):
    data = {'title': 'Презентации'}
    return render(request, 'educational_materials/presentations.html', context=data)


def textbooks(request):
    data = {'title': 'Учебники'}
    return render(request, 'educational_materials/textbooks.html', context=data)