from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('courses/<int:pk>/', views.course_detail, name='course_detail'),
    path('courses/<int:course_pk>/lessons/<int:pk>/', views.lesson_detail, name='lesson_detail'),
    path('enroll/<int:pk>/', views.enroll, name='enroll'),
    path('my-courses/', views.my_courses, name='my_courses'),
    path('signup/', views.signup, name='signup'),
]
