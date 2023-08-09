from django.contrib import admin
from .models import Todo
from django.contrib.auth.models import Group


# register todo
admin.site.register(Todo)

# unregister group
admin.site.unregister(Group)