from django.contrib import admin
from .models import Homework
from .models import Video
from .models import Audio
from .models import Textbooks
from .models import Source


admin.site.register(Homework)
admin.site.register(Video)
admin.site.register(Audio)
admin.site.register(Textbooks)

admin.site.register(Source)
