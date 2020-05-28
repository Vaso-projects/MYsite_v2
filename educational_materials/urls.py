from django.urls import path
from .views import index, video, homework, presentations, textbooks


urlpatterns = [
    path('', index),
    path('index', index),
    path('video', video),
    path('homework', homework),
    path('presentations', presentations),
    path('textbooks', textbooks)
]