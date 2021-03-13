import datetime
from django.core.files.storage import FileSystemStorage

from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.auth import models
from school_managment_app.models import CustomUser , Courses , Subjects, Staffs, Students, Class


def staff_home(request):
    return render(request, "staff/home-staff.html")

def show_staff(request):
    subjects = Subjects.objects.all()
    return render(request, "staff/show_staff_info.html",{"subjects": subjects})

def show_subject(request):
    subjects = Subjects.objects.all()
    return render(request, "staff/show_subject.html", {"subjects": subjects})