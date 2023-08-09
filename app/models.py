from django.db import models
from django.contrib.auth.models import User


class Todo (models.Model) :
    date = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=200)
    is_checked = models.BooleanField(default=False)

    def __str__(self) : 
        return f'{self.text} at {self.date.date()}' 