from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student

# Create your views here.
def home(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})

def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_no = request.POST.get('phone_no')
        course_name = request.POST.get('course_name')

        Student.objects.create(name=name, email=email, phone_no=phone_no, course_name=course_name)
        messages.success(request, 'New Student Added Successfully!!')
        
        return redirect('/')
        

    return render(request, 'add_student.html')


def update(request, student_id):
    student = Student.objects.get(id=student_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_no = request.POST.get('phone_no')
        course_name = request.POST.get('course_name')

        Student.objects.filter(id=student_id).update(name=name, email=email, phone_no=phone_no, course_name=course_name)
        messages.success(request, 'Student Updated Successfully!!')
        
        return redirect('/')

    return render(request, 'update_student.html', {'student': student})