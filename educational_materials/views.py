from django.shortcuts import render, redirect
from .models import Homework, Video, Audio, Textbooks
from .forms import HomeworkForm, HomeworkForm2
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse


def index(request):
    data = dict()
    data['title'] = 'Домашние задания'
    data['create_hw'] = Homework.objects.all()

    return render(request, 'educational_materials/index.html', context=data)


def create(request):
    data = dict()
    data['title'] = 'Создать домашнее задание'
    if request.method == "GET":
        data['form'] = HomeworkForm()
        return render(request, 'educational_materials/create_HW.html', context=data)
    elif request.method == 'POST':
        filled_form = HomeworkForm(request.POST, request.FILES)
        filled_form.save()
        return redirect('/educational_materials')


def add_video(request):
    data = {'title': 'Добавить видео'}
    return render(request, 'educational_materials/add_video.html', context=data)


def add_source(request):
    data = {'title': 'Добавить ссылку'}
    return render(request, 'educational_materials/add_source.html', context=data)


def details(request, homework_id):
    data = dict()
    data['user'] = 'Content_manager'
    data['title'] = 'Просмотр домашнего задания'
    data['work'] = Homework.objects.get(id=homework_id)
    return render(request, 'educational_materials/details.html', context=data)


def edit(request, homework_id):
    data = dict()
    data['title'] = 'Редактировать домашнее задание'
    work = Homework.objects.get(id=homework_id)
    if request.method == "GET":
        data['form'] = HomeworkForm2(instance=work)
        data['work'] = work
        return render(request, 'educational_materials/edit_HW.html', context=data)
    elif request.method == "POST":
        form2 = HomeworkForm2(request.POST)

        if form2.is_valid():
            work.title = form2.cleaned_data['topic']
            work.about = form2.cleaned_data['about']
            work.content = form2.cleaned_data['content']
            work.source = form2.cleaned_data['source']
            work.save()
        return redirect('/educational_materials')

    return render(request, 'educational_materials/edit_HW.html', context=data)


def delete(request, homework_id):
    data = dict()
    data['title'] = 'Удалить домашнее задание'
    work = Homework.objects.get(id=homework_id)
    if request.method == "GET":
        data['work'] = work
        return render(request, 'educational_materials/delete_HW.html', context=data)
    elif request.method == "POST":
        work.delete()
    return redirect('/educational_materials/', context=data)


def del_v(request):
    data = {'title': 'Удалить видео'}
    return render(request, 'educational_materials/del_v.html', context=data)


def del_a(request):
    data = {'title': 'Удалить аудио'}
    return render(request, 'educational_materials/del_a.html', context=data)


def homework(request):
    data = dict()
    data['title'] = 'Домашнее задание'
    return render(request, 'educational_materials/homework.html', context=data)


def video(request):
    data = {'title': 'Видео'}
    return render(request, 'educational_materials/video.html', context=data)


def source(request):
    data = dict()
    data['title'] = 'Рекомендованные ссылки'
    return render(request, 'educational_materials/source.html', context=data)


def audio(request):
    data = {'title': 'Аудио файлы'}
    return render(request, 'educational_materials/audio.html', context=data)


def textbooks(request):
    data = {'title': 'Учебники'}
    return render(request, 'educational_materials/textbooks.html', context=data)


def add_audio(request):
    data = {'title': 'Добавить аудио'}
    return render(request, 'educational_materials/add_audio.html', context=data)


def educational_materials(request):
    data = {'title': 'Учебные материалы'}
    return render(request, '/educational_materials/educational_materials.html', context=data)

