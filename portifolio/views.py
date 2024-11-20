from django.shortcuts import render
from portifolio.models import educacao, experiencia, projetos, skills, certificados


def index(request):

    return render(request, 'index.html')


def contact(request):

    return render(request, 'contact.html')


def resume(request):
    experiencia_list = experiencia.objects.all()
    educacao_list = educacao.objects.all()
    skills_list = skills.objects.all()
    certificados_list = certificados.objects.all()
    return render(request, 'resume.html', {
        'experiencias': experiencia_list,
        'educacoes': educacao_list,
        'skills': skills_list,
        'certificados': certificados_list
    })


def projects(request):
    projects_list = projetos.objects.all()
    return render(request, 'projects.html', {'projetos': projects_list})
