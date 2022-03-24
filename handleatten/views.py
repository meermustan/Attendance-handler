from datetime import date
from warnings import catch_warnings
from django.shortcuts import render,HttpResponse
from django.utils import timezone
from .models import Student,StudentsAttendance

# Create your views here.
def index(request):
    allStudents = Student.objects.all()
    tenthStudents = allStudents.filter(class_name="10")
    finalQuery = []
    
    for item in tenthStudents:
        finalQuery.append([item,StudentsAttendance.objects.filter(data=item)])



    # MonthDetails = []
    # for item in range(31):
    #     item = item+1
    #     my_date = date(2022,3,item)
    #     MonthDetails.append(my_date)



    params = {'students':finalQuery}
    return render(request,'index.html',params)