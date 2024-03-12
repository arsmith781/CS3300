from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views import generic

# for forms
from .forms import StudentForm, ProjectForm, PortfolioForm


def index(request):
    studentActivePortfolios = Student.objects.select_related('portfolio').all().filter(portfolio__is_active=True)
    return render(request, 'portfolio_app/index.html', {'studentActivePortfolios': studentActivePortfolios})

def createProject(request, portfolio_id):
    portfolio = Portfolio.objects.get(pk=portfolio_id)

    if request.method == 'POST':
        project_data = request.copy()
        project_data['portfolio_id'] = portfolio_id
        form = ProjectForm(project_data)
        if form.is_valid():
            # Save and dont commit to database
            project = form.save(commit=False)
            # create the portfolio -> project relationship
            project.portfolio = portfolio
            project.save()

            # Go to the portfolio detail page
            return redirect('portfolio-detail', pk=portfolio_id)
    else:
        form = ProjectForm()

    context = {'form': form}
    return render(request, 'portfolio_app/project_form.html', context)


# https://openclassrooms.com/en/courses/6967196-create-a-web-application-with-django/7349667-update-a-model-object-with-a-modelform
# portfolio id is not here but the url should look pretty so there ya go (in urls.py)
def updateProject(request, portfolio_id, project_id):
    project = Project.objects.get(pk=project_id)
    form = ProjectForm(instance=project)
    context = {'form': form}
    return render(request, 'portfolio_app/project_form.html', context)


# Views for models.py data
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

