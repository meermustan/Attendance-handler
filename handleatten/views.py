from django.shortcuts import render,HttpResponse
from .models import Student,StudentsAttendance

# Create your views here.
def index(request):
    allStudents = Student.objects.all()
    tenthStudents = allStudents.filter(class_name="10")
    finalQuery = []
    
    for item in tenthStudents:
        # print(StudentsAttendance.objects.filter(data=item).values())
        finalQuery.append([item,StudentsAttendance.objects.filter(data=item)])
    # print(finalQuery)
    




    params = {'students':finalQuery}
    return render(request,'index.html',params)