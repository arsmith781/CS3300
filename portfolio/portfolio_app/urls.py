from django.urls import path
from . import views

#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
urlpatterns = [
    path('', views.index, name='index'),
    # View and lists for models
    path('students/', views.StudentListView.as_view(), name='students'),
    path('student/<int:pk>', views.StudentDetailView.as_view(), name='student-detail'),
    path('portfolios/', views.PortfolioListView.as_view(), name='portfolios'),
    path('portfolio/<int:pk>', views.PortfolioDetailView.as_view(), name='portfolio-detail'),
    path('projects/', views.ProjectListView.as_view(), name='projects'),
    path('project/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),
    # Forms for models
    path('portfolio/<int:portfolio_id>/create_project/', views.createProject, name='create-project'),
    path('portfolio/<int:portfolio_id>/update_project/<int:project_id>', views.updateProject, name='update-project'),

]
