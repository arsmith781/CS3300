from django.forms import ModelForm
from .models import Student, Project, Portfolio
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'description',)


class PortfolioForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = ('title', 'contact_email', 'is_active', 'about',)


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'email', 'major',)


# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = 'name', 'email'