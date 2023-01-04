from django.shortcuts import render
from django.views import View
from django.db.models import Q
# Local apps
from .models import Student, Lesson, Teacher 


class StudentList(View):
	def get(self, request):
		students = Student.objects.all().values_list("name", "age")
		print(students)

		context = {'students': students}
		return render(request, 'university/index.html', context)
