import datetime
from django.core.files.storage import FileSystemStorage

from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.auth import models
from school_managment_app.models import CustomUser , Courses , Subjects, Staffs, Students, Class


def student_home(request):
    students = Students.objects.all()
    return render(request, "student/home-student.html", {"students": students})

