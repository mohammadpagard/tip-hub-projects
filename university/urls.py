from django.urls import path
from . import views


app_name = "university"
urlpatterns = [
	path('values/', views.StudentList.as_view(), name='students'),
	path('q-function/', views.LessonList.as_view(), name='lessons'),
]
