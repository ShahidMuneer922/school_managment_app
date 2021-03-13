"""school_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from school_managment_app import views
from school_managment_app import HODviews, Studentviews, Staffviews
from school_project import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path( '' , views.ShowLoginPage, name='school-login'),
    path('doLogin', views.doLogin, name='doLogin'),
    path('get_user_details', views.GetUserDetails, name='get_user_details'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('admin_home', HODviews.admin_home, name='admin_home'),
    path('add_staff', HODviews.add_staff, name='add_staff'),
    path('add_staff_save', HODviews.add_staff_save, name='add_staff_save'),
    path('add_course_save', HODviews.add_course_save, name='add_course_save'),
    path('add_course', HODviews.add_course, name='add_course'),
    path('add_student_save', HODviews.add_student_save, name='add_student_save'),
    path('add_student', HODviews.add_student, name='add_student'),
    path('add_subject_save', HODviews.add_subject_save, name='add_subject_save'),
    path('add_subject', HODviews.add_subject, name='add_subject'),
    path('manage_staff', HODviews.manage_staff, name='manage_staff'),
    path('manage_student', HODviews.manage_student, name='manage_student'),
    path('manage_subject', HODviews.manage_subject, name='manage_subject'),
    path('manage_course', HODviews.manage_course, name='manage_course'),
    path('manage_class', HODviews.manage_class, name='manage_class'),
    path('edit_staff/<str:staff_id>', HODviews.edit_staff, name='edit_staff'),
    path('edit_staff_save', HODviews.add_staff_save, name='edit_staff_save'),
    path('edit_student/<str:student_id>', HODviews.edit_student, name='edit_student'),
    path('edit_student_save', HODviews.add_student_save, name='edit_student_save'),
    path('edit_subject_save', HODviews.edit_subject_save, name='edit_subject_save'),
    path('edit_subject/<str:subject_id>', HODviews.edit_subject, name='edit_subject'),
    path('edit_course_save', HODviews.edit_course_save, name='edit_course_save'),
    path('edit_course/<str:course_id>', HODviews.edit_course, name='edit_course'),
    path('add_class', HODviews.add_class, name='add_class'),
    path('manage_session', HODviews.manage_session, name='manage_session'),
    path('add_session_save', HODviews.add_session_save, name="add_session_save"),

    # staff urls

    path('staff_home', Staffviews.staff_home, name="staff_home"),
    path('show_staff', Staffviews.show_staff, name='show_staff'),
    path('show_subject', Staffviews.show_subject, name='show_subject'),

    #student urls

    path('student_home', Studentviews.student_home, name='student_home'),





]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

