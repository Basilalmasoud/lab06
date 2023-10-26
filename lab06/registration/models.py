from django.db import models

class Course(models.Model):
    C_name=models.CharField(max_length=64)
    C_num=models.CharField(max_length=64)

    def __str__(self):
        return f"{self.C_name}: {self.C_num}"
    


class Student(models.Model):
    fname=models.CharField(max_length=64)
    lname=models.CharField(max_length=64)
    college=models.CharField(max_length=64)
    age=models.IntegerField()
    course=models.ManyToManyField(Course, blank=True, related_name="students")
    
    def __str__(self):
        return f"{self.id}: {self.fname} {self.lname}, age={self.age} goes to {self.college}"