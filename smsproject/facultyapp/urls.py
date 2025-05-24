from django.urls import path, include
from. import views

urlpatterns = [
    path("checkfacultylogin", views.checkfacultylogin, name="checkfacultylogin"),
    path("facultyhome", views.facultyhome, name="facultyhome"),
    path("facultycourses", views.facultycourses, name="facultycourses"),
    path("facultychangepw", views.facultychangepw, name="facultychangepw"),
    path("facultyupdatepw", views.facultyupdatepw, name="facultyupdatepw"),

]