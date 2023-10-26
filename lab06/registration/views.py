from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse

def courses(request):
    return render(request, "registration/courses.html",{
        "courses": Course.objects.all()
    })
def students(request):
    return render(request, "registration/students.html",{
        "students": Student.objects.all()
    })

class CourseModelForm(forms.ModelForm):
    class Meta:
        model=Course
        fields="__all__"

class StudentModelForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=["fname","lname","college","age"]

def addStudent(request):
    if request.method=="POST":
        form=StudentModelForm(request.POST)
        if (form.is_valid):
            form.save()
            return HttpResponseRedirect(reverse("students"))
        else:
            return render(request,"registration/createStudent.html",{
                "message": "invalid data entered for student."
            })
    else:
        return render(request, "registration/createStudent.html",{
            "form":StudentModelForm()
        })

def addcourse(request):
    if request.method=="POST":
        form=CourseModelForm(request.POST)
        if (form.is_valid):
            form.save()
            return HttpResponseRedirect(reverse("courses"))
        else:
            return render(request,"registration/createCourse.html",{
                "message": "invalid data entered for course."
            })
    else:
        return render(request, "registration/createCourse.html",{
            "form":CourseModelForm()
        })


def details(reqeust, student_id):
    student=Student.objects.get(pk=student_id)
    not_registered=Course.objects.exclude(id__in=student.course.all())
    registered=student.course.all()
    if reqeust.method=="POST":
        selected_course_id=reqeust.POST.get('course')
        selected_course=Course.objects.get(id=selected_course_id)
        student.course.add(selected_course)

        return redirect("details",student_id=student_id)
    else:
        return render(reqeust, "registration/details.html",{
            "studetn":student,
            "not_registered":not_registered,
            "registered": registered
        })