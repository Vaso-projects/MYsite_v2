from django.urls import path
from .views import sign_in, sign_up, sign_up_res, sign_out, ajax_reg


urlpatterns = [
    path('sign_up', sign_up),
    path('sign_in', sign_in),
    path('sign_out', sign_out),
    path('sign_up_res', sign_up_res),
    path('ajax_reg', ajax_reg)

]
