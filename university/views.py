from django.shortcuts import render
from django.views import View
from django.db.models import Q
# Local apps
from .models import Student, Lesson, Teacher 


# values AND values_list
class StudentList(View):
	def get(self, request):
		students = Student.objects.all().values_list("name", "age")
		print(students)

		context = {'students': students}
		return render(request, 'university/values_valueslist.html', context)


# Q-functions
class LessonList(View):
	def get(self, request):
		lessons = Lesson.objects.filter(
			Q(teacher__name="Amir Amiri") &
			Q(students__name="Danial")
		)

		context = {'lessons': lessons}
		return render(request, 'university/q_function.html', context)
