
from django.urls import path

from .views import control_users

urlpatterns = [
    path('control_users', control_users),


    # url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='user_logout'),
]
