from django.urls import path
from .views import index, about, blog, contact


urlpatterns = [
    path('', index),
    path('index', index),
    path('about', about),
    path('blog', blog),
    path('contact', contact)
]