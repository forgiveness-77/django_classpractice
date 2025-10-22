from django.urls import path
from . import views

urlpatterns = [
    path('attendance_list', views.attendance_list, name='attendance_list'),
    path('add_student/', views.add_student, name='add_student'),
    path('mark_attendance/', views.mark_attendance, name='mark_attendance')
]