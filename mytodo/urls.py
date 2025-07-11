from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="mytodo_home"),
    path('mark_completed/<int:task_id>/', views.mark_completed, name='mark_completed'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('add_task/', views.add_task, name='add_task'),
]