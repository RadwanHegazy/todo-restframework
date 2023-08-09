from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name='home'),
    path('edit/<int:todoid>/',views.edit_todo,name='edit'),


]