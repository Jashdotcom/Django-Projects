from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, StudentForm
from .models import Student
from django.shortcuts import get_object_or_404


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
    else:
        form = AuthenticationForm(request)

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/login')

    return redirect('/login')

@login_required
def student_list(request):
    students = Student.objects.all()
    return render(
        request,
        'student_list.html',
        {'students': students}
    )

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
def edit_student(request):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = Student(instance=student)

    return render(request, 'student_form.html', {'form': form, 'student': student})
        





