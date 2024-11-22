from django.shortcuts import render
from portifolio.models import educacao, experiencia, projetos, skills, certificados


def index(request):

    return render(request, 'index.html')


def contact(request):

    return render(request, 'contact.html')


def resume(request):
    experiencia_list = experiencia.objects.all().order_by('-id')
    educacao_list = educacao.objects.all().order_by('-id')
    skills_list = skills.objects.all()
    certificados_list = certificados.objects.all().order_by('-id')
    return render(request, 'resume.html', {
        'experiencias': experiencia_list,
        'educacoes': educacao_list,
        'skills': skills_list,
        'certificados': certificados_list
    })


def projects(request):
    projects_list = projetos.objects.all().order_by('-id')
    return render(request, 'projects.html', {'projetos': projects_list})
