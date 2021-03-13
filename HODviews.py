import datetime
from django.core.files.storage import FileSystemStorage

from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.auth import models
from school_managment_app.models import CustomUser , Courses , Subjects, Staffs, Students, SessionYearModel
from django.urls import reverse


def admin_home(request):
    return render ( request , "HOD/home.html" )


def add_staff(request):
    return render ( request , "HOD/add_staff.html" )


def add_staff_save(request):
    if request.method != "POST":
        return HttpResponse ( "Method Not Allowed" )
    else:
        email = request.POST.get ( "email" )
        password = request.POST.get ( "password" )
        first_name = request.POST.get ( "first_name" )
        last_name = request.POST.get ( "last_name" )
        username = request.POST.get ( "username" )
        # address = request.POST.get("address")
        try:
            user = CustomUser.objects.create_user ( username=username , password=password , email=email ,
                                                    last_name=last_name , first_name=first_name , user_type=2 )
            # user.staffs.address = address
            user.save ()
            messages.success ( request , "Staff Added Successfully" )
            return HttpResponseRedirect ( "/admin_home" )
        except:
            messages.error ( request , "Unexpected Error Occurred" )
            return HttpResponseRedirect ( "/add_staff" )


def add_course(request):
    return render(request, 'HOD/add_course.html' )


def add_course_save(request):
    if request.method != "POST":
        return HttpResponse ( "Method Not Allaowed" )
    else:
        course = request.POST.get ( "course" )
        try:
            course_model = Courses ( course_name=course )
            course_model.save ()
            messages.success ( request , "Successfully Added Course" )
            return HttpResponseRedirect ( "/add_course" )
        except:
            messages.error ( request , "Failed To Add" )
            return HttpResponseRedirect ( "/add_course" )


def add_student(request):
    courses = Courses.objects.all ()
    return render ( request , "HOD/add_student.html" , {"courses": courses} )


def add_student_save(request):
    if request.method != "POST":
        return HttpResponse ( "Method Not Allowed" )
    else:
        email = request.POST.get ( "email" )
        password = request.POST.get ( "password" )
        first_name = request.POST.get ( "first_name" )
        last_name = request.POST.get ( "last_name" )
        username = request.POST.get ( "username" )
        address = request.POST.get ( "address" )
        session_start = request.POST.get("session_start")
        session_end = request.POST.get("session_end")
        course_id = request.POST.get("course")
        gender = request.POST.get("gender")

        profile_pic = request.FILES['profile_pic']
        fs = FileSystemStorage()
        filename = fs.save(profile_pic.name, profile_pic)
        profile_pic_url = fs.url(filename)


        try:
            user = CustomUser.objects.create_user(username=username , password=password , email=email, last_name=last_name, first_name=first_name, user_type=3)
            user.students.address = address
            course_obj = Courses.objects.get(id=course_id)
            user.students.course_id = course_obj
            user.students.session_start_year = session_start
            user.students.session_end_year = session_end
            user.students.gender = gender
            user.students.profile_pic = profile_pic_url
            user.save ()
            messages.success(request, "Student Added Successfully")
            return HttpResponseRedirect("/admin_home")
        except Exception as e:
            print(e)
            messages.error ( request , "Unexpected Error Occoured", e )
            return HttpResponseRedirect("/add_student")


def add_subject(request):
    courses = Courses.objects.all ()
    staffs = CustomUser.objects.filter ( user_type=2 )
    return render(request, "hod/add_subject.html", {"staffs": staffs, "courses": courses})


def add_subject_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        subject_name = request.POST.get("subject_name")
        course_id = request.POST.get("course")
        course = Courses.objects.get(id=course_id)
        staff_id = request.POST.get("staff")
        staff = CustomUser.objects.get(id=staff_id)

        try:
            subject = Subjects ( subject_name=subject_name , course_id=course,staffs_id=staff )
            subject.save ()
            messages.success ( request , "Successfully Added Subject" )
            return HttpResponseRedirect( "/admin_home")
        except:
            messages.error ( request , "An Unexpected Error Occurred" )
            return HttpResponseRedirect ( "/add_subject" )


def manage_staff(request):
    staffs = Staffs.objects.all()
    return render(request, "HOD/manage_staff.html", {"staffs" : staffs})


def manage_student(request):
    students = Students.objects.all()
    return render(request, "HOD/manage_student.html", {"students": students})


def manage_subject(request):
    subjects = Subjects.objects.all()
    return render(request, "HOD/manage_subject.html", {"subjects": subjects})

def manage_course(request):
    courses = Courses.objects.all()
    return render(request, "HOD/manage_course.html", {"courses": courses})

def manage_class(request):
    courses = Courses.objects.all ()
    subjects = Subjects.objects.all()
    staffs = CustomUser.objects.filter(user_type=2)

    return render ( request , "HOD/manage_class.html" , {"courses": courses, "subjects": subjects, "staffs":staffs} )

def edit_staff(request, staff_id):
    staff = Staffs.objects.get(admin=staff_id)
    return render(request,"hod/edit_staff.html" ,{"staff": staff})

def edit_staff_save(request):
    if request.method != "POST":
        return HttpResponse("<h2> Method Not Allowed</h2>")
    else:
        staff_id = request.POST.get("staff_id")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        try:
            user = CustomUser.objects.get(id=staff_id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.username = username
            user.save()

            staff_model = Staffs.objects.get(admin=staff_id)
            staff_model.save()
            messages.success(request, "Successfully Edited Staff" )
            return HttpResponseRedirect("/admin_home")
        except:
            messages.error(request, "An Unexpected Error Occurred" )
            return HttpResponseRedirect("/edit_staff/")

def edit_student(request, student_id):
    courses = Courses.objects.all()
    student = Students.objects.get(admin= student_id)
    return render(request, "HOD/edit_student.html", {"student": student, "courses": courses})


def edit_student_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        student_id = request.POSt.get("student_id")
        email = request.POST.get ( "email" )
        first_name = request.POST.get ( "first_name" )
        last_name = request.POST.get ( "last_name" )
        username = request.POST.get ( "username" )
        address = request.POST.get ( "address" )
        session_start = request.POST.get ( "session_start" )
        session_end = request.POST.get ( "session_end" )
        course_id = request.POST.get ( "course" )
        gender = request.POST.get ( "gender" )
        user = CustomUser.objects.get(id=student_id)


        if request.FILES['profile_pic']:
            profile_pic = request.FILES['profile_pic']
            fs = FileSystemStorage()
            filename = fs.save(profile_pic.name, profile_pic)
            profile_pic_url = fs.url(filename)
        else:
            profile_pic_url = None
        try:
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.email = email
            user.save()

            student = Students.objects.get(admin = student_id)
            student.address = address
            student.session_start_year = session_start
            student.session_end_year = session_end
            student.gender = gender

            course = Courses.objects.get(id=course_id)
            student.course_id = course
            if profile_pic_url != None:
                student.profile_pic = profile_pic_url
            student.save()
            messages.success(request, "Successfully Edited Student" )
            return HttpResponseRedirect("/admin_home"+student_id)
        except:
            messages.error(request, "An Unexpected Error Occurred" )
            return HttpResponseRedirect("/edit_student/"+student_id)

def edit_subject (request, subject_id):
    subject = Subjects.objects.get(id=subject_id)
    courses = Courses.objects.all()
    staffs = CustomUser.objects.filter(user_type=2)
    return render(request, "HOD/edit_subject.html", {"subject": subject, "courses": courses, "staffs": staffs})

def edit_subject_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        subject_id = request.POST.get("subject_id")
        subject_name = request.POST.get("subject_name")
        staff_id = request.POST.get("staff")
        course_id = request.POST.get("course")
        try:
            subject = Subjects.objects.get(id=subject_id)
            subject.subject_name = subject_name
            staff = CustomUser.objects.get(id=staff_id)
            subject.staff_id = staff
            course = Courses.objects.get(id=course_id)
            subject.course_id = course
            subject.save()
            messages.success(request, "Successfully Edited Subject")
            return HttpResponseRedirect("/edit_subject/"+subject_id)
        except Exception as e:
            print ( e )
            messages.error(request, "An Unexpected Error Occurred")
            return HttpResponseRedirect("HOD/manage_subject"+subject_id)

def edit_course(request, course_id):
    course = Courses.objects.get(id=course_id)
    return render(request, "HOD/edit_course.html", {"course": course})

def edit_course_save(request):
    if request.method != "POST":
        return HttpResponse("Methord Not Allowed")
    else:
        course_id = request.POST.get("course_id")
        course_name = request.POST.get("course")
        try:
            course = Courses.objects.get(id=course_id)
            course.course_name = course_name
            course.save()
            messages.success ( request , "Successfully Edited Course")
            return HttpResponseRedirect ("/edit_course/" + course_id)
        except:
            messages.error ( request , "An Unexpected Error Occurred" )
            return HttpResponseRedirect ( "/edit_course/" + course_id )

def add_class(request):
    courses = Courses.objects.all ()
    subjects = Subjects.objects.all()
    staffs = CustomUser.objects.filter(user_type=2)

    return render ( request , "HOD/add_class.html" , {"courses": courses, "subjects": subjects, "staffs":staffs} )
def add_class_save(request):
    pass

def manage_session(request):
    return render(request, "HOD/manage_session.html")

def add_session_save(request):
    if request.method != "POST":
        return HttpResponseRedirect(reverse("manage_session"))
    else:
        session_start_year = request.POST.get("session_start")
        session_end_year = request.POST.get("session_end")
        try:
            sessionyear = SessionYearModel(session_start_year=session_start_year, session_end_year=session_end_year)
            sessionyear.save()
        except:
            messages.error("Failed to add Session")
            return HttpResponseRedirect(reverse("manage_session"))
