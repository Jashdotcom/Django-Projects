from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Student


class RegistrationForm(UserCreationForm):
    pass

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'course', 'email']

    def clean_name(self):
        name=self.cleaned_data['name'].strip()

        if len(name)<2:
            raise forms.ValidationError(
                'Name must contain at least 2 characters'
            )
        return name

    def clean_age(self):
        age=self.cleaned_data['age']

        if age<1 or age>120:
            raise forms.ValidationError(
                'Age must be between 1 & 120'
            )
        return age

    def clean_course(self):
        course=self.cleaned_data['course'].strip()

        if len(course)<2:
            raise forms.ValidationError(
                'Course must contain at least 2 characters'
            )
        return course
