
from django.urls import path

from .views import sign_in, sign_up, report, profile,  logout1, ajax_reg


urlpatterns = [
    path('sign_up', sign_up),
    path('sign_in', sign_in),
    path('logout1', logout1),
    path('report', report),
    path('ajax_reg', ajax_reg),
    path('profile', profile)
    # url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='user_logout'),
]
