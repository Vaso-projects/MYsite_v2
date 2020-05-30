from django.shortcuts import render, redirect
from .models import CreateHW
from .forms import CreateHWForm


def index(request):
    data = dict()
    data['user'] = 'temp_admin'
    data['title'] = 'Учебный материал'
    data['create_hw'] = CreateHW.objects.all()
    return render(request, 'educational_materials/index.html', context=data)


def create(request):
    data = dict()
    data['title'] = 'Создать домашнее задание'
    if request.method == "GET":
        data['form'] = CreateHWForm()
        return render(request, 'educational_materials/create_HW.html', context=data)
    elif request.method == 'POST':
        filled_form = CreateHWForm(request.POST, request.FILES)
        filled_form.save()
        return redirect('/educational_materials')


def edit(request):
    data = {'title': 'Редактировать домашнее задание'}
    return render(request, 'educational_materials/edit_HW.html', context=data)


def delete(request):
    data = {'title': 'Удалить домашнее задание'}
    return render(request, 'educational_materials/delete_HW.html', context=data)


def del_v(request):
    data = {'title': 'Удалить видео'}
    return render(request, 'educational_materials/del_v.html', context=data)


def del_a(request):
    data = {'title': 'Удалить аудио'}
    return render(request, 'educational_materials/del_a.html', context=data)


def homework(request):
    data = {'title': 'Домашнее задание'}
    return render(request, 'educational_materials/homework.html', context=data)


def video(request):
    data = {'title': 'Видео'}
    return render(request, 'educational_materials/video.html', context=data)


def audio(request):
    data = {'title': 'Аудио файлы'}
    return render(request, 'educational_materials/audio.html', context=data)


def textbooks(request):
    data = {'title': 'Учебники'}
    return render(request, 'educational_materials/textbooks.html', context=data)


def add_audio(request):
    data = {'title': 'Добавить аудио'}
    return render(request, 'educational_materials/add_audio.html', context=data)


def add_video(request):
    data = {'title': 'Добавить видео'}
    return render(request, 'educational_materials/add_video.html', context=data)


def add_source(request):
    data = {'title': 'Добавить ссылку'}
    return render(request, 'educational_materials/add_source.html', context=data)


def educational_materials(request):
    data = {'title': 'Учебные материалы'}
    return render(request, 'educational_materials/educational_materials.html', context=data)

