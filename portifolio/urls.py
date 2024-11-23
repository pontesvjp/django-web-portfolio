from django.urls import path
from portifolio.views import index, contact, resume, projects

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('resume/', resume, name='resume'),
    path('projects/', projects, name='projects'),

]
