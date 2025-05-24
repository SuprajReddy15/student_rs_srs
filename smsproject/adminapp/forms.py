from django import forms

from .models import Faculty, Student,FCourseMappings


class AddFacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = "__all__"
        exclude = {"password",}
        labels = {"facultyid":"Enter Faculty ID"}

class AddStudentForm(forms.ModelForm):
            class Meta:
                model = Student
                fields = "__all__"
                exclude = {"password", }
                labels = {"studentid": "Enter Student ID"}

class AddFCourseMappingForm(forms.ModelForm):
            class Meta:
                model = FCourseMappings
                fields = "__all__"
