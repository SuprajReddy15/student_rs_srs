from django.contrib import admin
from django.urls import path, include
from. import views

urlpatterns = [
    path("adminhome",views.adminhome,name="adminhome" ),
    path("logout",views.logout,name="logout"),
    path("checklogin",views.checklogin,name="checklogin"),

    path("viewcourses", views.viewcourses, name="viewcourses"),
    path("viewfaculty", views.viewfaculty, name="viewfaculty"),
    path("viewstudents", views.viewstudents, name="viewstudents"),

    path("admincourse",views.admincourse,name="admincourse" ),
    path("adminfaculty",views.adminfaculty,name="adminfaculty" ),
    path("adminstudent",views.adminstudent,name="adminstudent" ),

    path("addcourse",views.addcourse,name="addcourse" ),
    path("insertcourse", views.insertcourse, name="insertcourse"),
    path("deletecourse",views.deletecourse,name="deletecourse" ),
    path("cdelete/<int:cid>", views.cdelete, name="cdelete"),

    path("addfaculty",views.addfaculty,name="addfaculty" ),
    path("deletefaculty",views.deletefaculty,name="deletefaculty" ),
    path("fdelete/<int:fid>", views.fdelete, name="fdelete"),

    path("fcoursemapping", views.fcoursemapping, name="fcoursemapping"),
    path("addfcoursemapping/", views.addFCourseMapping, name="addfcoursemapping"),
    path("viewfcoursemapping/", views.viewfcoursemapping, name="viewfcoursemapping"),
    path("deletefcoursemapping",views.deletefcoursemapping,name="deletefcoursemapping" ),
    path("fcoursemappingdelete/<int:mapid>", views.fcoursemappingdelete, name="fcoursemappingdelete"),


    path("addstudent",views.addstudent,name="addstudent" ),
    path("deletestudent", views.deletestudent, name="deletestudent"),
    path("studentdelete/<int:sid>", views.studentdelete, name="studentdelete"),

    path("adminchangepw", views.adminchangepw, name="adminchangepw"),
    path("adminupdatepw", views.adminupdatepw, name="adminupdatepw"),
    path("signup", views.signup, name="signup"),

]
