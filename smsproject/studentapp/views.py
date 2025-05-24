from django.db.models import Q
from django.shortcuts import render

from adminapp.models import Student,Course,Faculty,FCourseMappings,Studentcoursemapping




# Create your views here.
def studenthome(request):
    sid=request.session["sid"]
    return render(request,"studenthome.html",{"sid":sid})



def checkstudentlogin(request):
    sid=request.POST["sid"]
    pwd=request.POST["pwd"]

    flag=Student.objects.filter(Q(studentid=sid)&Q(password=pwd))
    print(flag)

    if flag:
        print("Login Success")
        request.session["sid"] = sid  #creating a session
        return render(request,"studenthome.html",{"sid":sid})
        #return HttpResponse("login success")
    else:
        msg="Login Failed"
        return render(request,"studentlogin.html",{"message":msg})
        #return HttpResponse("login failed ")

def studentchangepw(request):
    sid = request.session["sid"]
    return render(request,"studentchangepw.html",{"sid":sid})


def studentupdatepw(request):
    sid = request.session["sid"]
    opwd=request.POST["opwd"]
    npwd = request.POST["npwd"]
    print(sid,opwd,npwd)

    flag=Student.objects.filter(Q(studentid=sid)&Q(password=opwd))
    if flag:
        print("old pw is correct")
        Student.objects.filter(studentid=sid).update(password=npwd)
        print("updated...")
        msg = "password updated"
    else:
        print("old pw is wrong")
        msg = "old password wrong"

    return render(request,"studentchangepw.html",{"sid":sid,"message":msg})


def studentcourses(request):
    sid = request.session["sid"]
    return render(request,"studentcourses.html",{"sid":sid})

def studentcoursemapping(request):

    syear=request.POST["Year"]
    semester=request.POST["semester"]
    filtered_courses=Course.objects.filter(Q(Year=syear)&Q(semester=semester))
    # print(filtered_courses[0].coursecode)
    # print(filtered_courses[0].coursetitle)
    # print(filtered_courses[0].Year)
    # print(filtered_courses[0].semester)
    for i in range(0,len(filtered_courses)):
        studentcmapping = Studentcoursemapping.objects.create(coursecode=filtered_courses[i].coursecode, coursetitle=filtered_courses[0].coursetitle, year=filtered_courses[0].Year,
                                                              semester=filtered_courses[0].semester)
        studentcmapping.save()
    if filtered_courses:

      return render(request,"studentcoursemapping.html",{"coursedata":filtered_courses})
    else :
       return render(request,"studentcourses.html")

def studentfacultymapping(request):
    temp=Studentcoursemapping.objects.last()
    print(temp.year)
    filtered_courses = Course.objects.filter(Q(Year=temp.year) & Q(semester=temp.semester))
    course_with_id = Course.objects.filter(coursetitle=filtered_courses[0])
    print(course_with_id[0].id)
    cid = course_with_id[0].id
    fid = FCourseMappings.objects.filter(Course_id=cid)
    fid = fid[0].faculty_id
    faculty_details = Faculty.objects.filter(facultyid=4656)
    return render(request,"studentfacultymapping.html",{"fdetails":faculty_details})