
from django.shortcuts import render, redirect
from hashlib import md5
from datetime import datetime

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core.paginator import Paginator


def control_users(request):
    data = dict()
    all_user = User.objects.all()

    data['users'] = all_user

    paginator = Paginator(all_user, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data['page_obj'] = page_obj
    return render(request, 'control/control_users.html', context=data)


