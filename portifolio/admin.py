from django.contrib import admin
from portifolio.models import experiencia, projetos, educacao, skills, certificados


admin.site.register(experiencia)
admin.site.register(projetos)
admin.site.register(educacao)
admin.site.register(skills)
admin.site.register(certificados)


class ListandoExperiencias(admin.ModelAdmin):
    list_display = ("id", "funcao", "empresa")
    list_display_links = ("id", "funcao",)
    search_fields = ("empresa",)


class ListandoProjetos(admin.ModelAdmin):
    list_display = ("id", "nome_projeto")
    list_display_links = ("id", "nome_projeto")
    search_fields = ("nome_projeto",)

class ListandoEducacoes(admin.ModelAdmin):
    list_display = ("id", "colegio") 
    list_display_links= ("id", "colegio")
    search_fields=("colegio")
    
class ListandoSkills(admin.ModelAdmin):
    list_display = ("id", "skill")
    list_display_links=("id", "skill")
    search_fields=("skill")
    
class ListandoCertificados(admin.ModelAdmin):
    list_display = ("id", "nome_cert", "local_cert")
    list_display_links=("id", "nome_cert")
    search_fields=("nome_cert")