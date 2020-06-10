
from django.shortcuts import render, redirect
from hashlib import md5
from datetime import datetime

from educational_materials.models import User, Group
from django.http import JsonResponse
from django.core.paginator import Paginator


def control_users(request):
    data = dict()
    data['title'] = 'Ваши студенты'
    all_user = User.objects.all()
    all_group = Group.objects.all()
    data['users'] = all_user
    data['groups'] = all_group

    paginator = Paginator(all_user, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data['page_obj'] = page_obj
    return render(request, 'control/control_users.html', context=data)


