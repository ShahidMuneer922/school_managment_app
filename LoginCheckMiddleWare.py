from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class LoginCheckMiddleWare(MiddlewareMixin):

    def process_view(self,request,view_func,view_args,view_kwargs):
        modulename = view_func.__module__
        user = request.user
        if user.is_authenticated:
            if user.user_type == "1":
                if modulename == "school_managment_app.Hodviews":
                    pass
                elif modulename == "school_managment_app.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("admin_home"))
            elif user.user_type == "2":
                if modulename == "school_managment_app.Staffviews":
                    pass
                elif modulename == "school_managment_app.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("staff_home"))
            elif user.user_type == "3":
                if modulename == "school_managment_app.Studentviews":
                    pass
                elif modulename == "school_managment_app.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("student_home"))
            else:
                return HttpResponseRedirect(reverse("school-login"))

        else:
            if request.path == reverse("school-login") or request.path == reverse("doLogin"):
                pass
            else:
                return HttpResponseRedirect(reverse("school-login"))