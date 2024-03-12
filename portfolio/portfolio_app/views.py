from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views import generic


def index(request):
    studentActivePortfolios = Student.objects.select_related('portfolio').all().filter(portfolio__is_active=True)
    return render(request, 'portfolio_app/index.html', {'studentActivePortfolios': studentActivePortfolios})


class StudentListView(generic.ListView):
    model = Student


class StudentDetailView(generic.DetailView):
    model = Student


class PortfolioListView(generic.ListView):
    model = Portfolio


class PortfolioDetailView(generic.DetailView):
    model = Portfolio


class ProjectListView(generic.ListView):
    model = Project


class ProjectDetailView(generic.DetailView):
    model = Project

