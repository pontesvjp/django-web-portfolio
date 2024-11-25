from django.shortcuts import render
from django.http import JsonResponse
from portifolio.models import educacao, experiencia, projetos, skills, certificados, contato


def index(request):

    return render(request, 'index.html')


def contact(request):
    if request.method == "POST":
        nome = request.POST.get('name')
        email = request.POST.get('email')
        telefone = request.POST.get('phone')
        mensagem = request.POST.get('message')

        if nome and email and mensagem:
            contato.objects.create(
                nome=nome, email=email, telefone=telefone, mensagem=mensagem
            )
            return JsonResponse({"success": True, "message": "Formulário enviado com sucesso!"})
        return JsonResponse({"success": False, "message": "Todos os campos são obrigatórios!"})
    
    return render(request, 'contact.html')


def resume(request):
    experiencia_list = experiencia.objects.all().order_by('id')
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
