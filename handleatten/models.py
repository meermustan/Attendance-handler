from pyexpat import model
from django.db import models
from django.utils import timezone

# Create your models here.

class Student(models.Model):
    data = models.CharField(max_length=30)
    class_name = models.CharField(max_length=50)

    def __str__(self):
        return self.data

class StudentsAttendance(models.Model):
    data = models.ForeignKey(Student,on_delete=models.DO_NOTHING)
    attendance = models.CharField(max_length=20)
    on_create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.attendance

    def on_save(self):
        student = Student.objects.filter(data=self.data)
        print(student)
        # if student.attendance:


    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})

