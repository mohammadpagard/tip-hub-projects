from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=2)
    about = models.TextField(default="This is a student")

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student)
    teacher = models.ForeignKey("Teacher", on_delete=models.CASCADE, related_name='lesson')
    description = models.TextField()

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=2)
    lessons = models.ManyToManyField(Lesson)
    about = models.TextField(default="This is a teacher")

    def __str__(self):
        return self.name

