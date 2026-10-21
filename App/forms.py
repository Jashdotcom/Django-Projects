from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Student


class RegistrationForm(UserCreationForm):
    pass

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'course', 'email']