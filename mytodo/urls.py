from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="mytodo_home"),
    path('mark_completed/<int:task_id>/', views.mark_completed, name='mark_completed'),
]