from django.urls import path
from . import views


urlpatterns =[
    path("courses", views.courses, name="courses"),
    path("students", views.students, name="students"),
    path("createStudent", views.addStudent, name="createStudent"),
    path("createCourse", views.addcourse, name="createCourse"),
    path("<int:student_id>", views.details, name="details")
    
]