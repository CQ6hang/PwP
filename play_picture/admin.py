from django.contrib import admin

# Register your models here.
from play_picture.models import User, Suggestion, Picture, Task, Suggester

admin.site.register(User)
admin.site.register(Suggestion)
admin.site.register(Suggester)
admin.site.register(Picture)
admin.site.register(Task)
