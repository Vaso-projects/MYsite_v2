from django.urls import path
from .views import index, video,  textbooks, create,\
    edit, delete, audio, add_audio, add_source, add_video, del_a,\
    del_v
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', index),
    path('index', index),
    path('audio', audio),
    path('add_audio', add_audio),
    path('add_source', add_source),
    path('add_video', add_video),
    path('create', create),
    path('del_a', del_a),
    path('del_v', del_v),
    path('delete', delete),
    path('edit', edit),
    path('textbooks', textbooks),
    path('video', video),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
