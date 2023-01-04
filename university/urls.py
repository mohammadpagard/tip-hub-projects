from django.urls import path
from . import views


app_name = "university"
urlpatterns = [
	path('', views.StudentList.as_view(), name='students'),
]
