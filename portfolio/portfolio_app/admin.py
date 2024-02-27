from django.contrib import admin
from .models import Student, Project, Portfolio

# Register your models here.
admin.site.register(Student)
admin.site.register(Project)
admin.site.register(Portfolio)