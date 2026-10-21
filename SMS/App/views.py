from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, StudentForm
from .models import Student
from django.shortcuts import get_object_or_404
from django.db import models


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if  form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = RegistrationForm()
            
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('student_list')
    else:
        form = AuthenticationForm(request)

    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def student_list(request):
    query = request.GET.get('q', '').strip()

    students = Student.objects.all()

    if query:
        students = students.filter(
            models.Q(name__icontains=query) |
            models.Q(course__icontains=query) |
            models.Q(email__icontains=query)
        )

    return render(request, 'student_list.html', {
        'students': students,
        'query': query
    })


@login_required
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:
        form = StudentForm()

    return render(request, 'student_form.html', {'form': form} )

@login_required
def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'student_form.html', {'form': form, 'student': student})

@login_required
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(request, 'student_confirm_delete.html', {'student': student})


        





