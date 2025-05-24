from django.db.models import Q
from django.shortcuts import render

from adminapp.models import FCourseMappings, Faculty,Course



# Create your views here.
def facultyhome(request):
    fid=request.session["fid"]
    return render(request,"facultyhome.html",{"fid":fid})

def checkfacultylogin(request):
    fid=request.POST["fid"]
    pwd=request.POST["pwd"]

    flag=Faculty.objects.filter(Q(facultyid=fid)&Q(password=pwd))
    print(flag)

    if flag:
        print("Login Success")
        request.session["fid"] = fid  #creating a session
        return render(request,"facultyhome.html",{"fid":fid})
        #return HttpResponse("login success")
    else:
        msg="Login Failed"
        return render(request,"facultylogin.html",{"message":msg})
        #return HttpResponse("login failed ")


def facultycourses(request):
    fid=request.session["fid"]

    mappingcourses=FCourseMappings.objects.all()
    fmcourses=[]
    for course in mappingcourses :
        if(course.faculty.facultyid==int(fid)):
            fmcourses.append(course)

    print(fmcourses)
    dir(fmcourses)
    count=len(fmcourses)
    return render(request,"facultycourses.html",{"fid":fid,"fmcourses":fmcourses,"count":count})


def facultychangepw(request):
    fid = request.session["fid"]
    return render(request,"facultychangepw.html",{"fid":fid})


def facultyupdatepw(request):
    fid = request.session["fid"]
    opwd=request.POST["opwd"]
    npwd = request.POST["npwd"]
    print(fid,opwd,npwd)

    flag=Faculty.objects.filter(Q(facultyid=fid)&Q(password=opwd))
    if flag:
        print("old pw is correct")
        Faculty.objects.filter(facultyid=fid).update(password=npwd)
        print("updated...")
        msg = "password updated"
    else:
        print("old pw is wrong")
        msg = "old password wrong"

    return render(request,"facultychangepw.html",{"fid":fid,"message":msg})