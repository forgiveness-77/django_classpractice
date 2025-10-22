from django.db import models
from django.utils import timezone


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    classroom = models.CharField(max_length=50)
    

    class Meta:
        db_table= 'students'

    def __str__(self):
        return self.name + " "+ self.classroom

class Attendance(models.Model):
    student= models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    present = models.BooleanField(default=False)

    class Meta:
        db_table='attendance' 

    def __str__(self):
        return self.student.name+ " " + self.student.classroom 
