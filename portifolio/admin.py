from django.contrib import admin
from .models import experiencia, educacao, skills, projetos, certificados, contato

from django.contrib import admin

admin.site.site_header = "Meu Sistema Admin"
admin.site.site_title = "Administração do Sistema"
admin.site.index_title = "Bem-vindo à Administração"


# Ações personalizadas
def marcar_como_atualizado(modeladmin, request, queryset):
    queryset.update(data="Atualizado")
marcar_como_atualizado.short_description = "Marcar como Atualizado"

# Admin para 'experiencia'
class ExperienciaAdmin(admin.ModelAdmin):
    list_display = ('funcao', 'empresa', 'data', 'local')
    search_fields = ('funcao', 'empresa')
    list_filter = ('data',)
    actions = [marcar_como_atualizado]  # Ação personalizada

# Admin para 'educacao'
class EducacaoAdmin(admin.ModelAdmin):
    list_display = ('colegio', 'especialidade', 'data', 'local')
    search_fields = ('colegio', 'especialidade')
    list_filter = ('data',)
    list_editable = ('especialidade',)  # Permite editar o campo diretamente na lista

# Admin para 'skills'
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('skill',)
    search_fields = ('skill',)
    list_filter = ('skill',)  # Filtro baseado em 'skill'
    ordering = ['skill']  # Ordenação personalizada por 'skill'

# Admin para 'projetos'
class ProjetosAdmin(admin.ModelAdmin):
    list_display = ('nome_projeto', 'url_projeto', 'descricao', 'foto')
    search_fields = ('nome_projeto', 'descricao')
    list_filter = ('nome_projeto',)
    ordering = ['nome_projeto']  # Ordenação personalizada
    readonly_fields = ('url_projeto',)  # Torna o campo 'url_projeto' somente leitura

# Admin para 'certificados'
class CertificadosAdmin(admin.ModelAdmin):
    list_display = ('nome_cert', 'data_cert', 'local_cert', 'descricao_cert', 'url_cert')
    search_fields = ('nome_cert', 'descricao_cert')
    list_filter = ('data_cert',)
    ordering = ['data_cert']  # Ordenação personalizada
    readonly_fields = ('url_cert',)  # Torna o campo 'url_cert' somente leitura

# Admin para 'contato'
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'criado_em')
    search_fields = ('nome', 'email')
    list_filter = ('criado_em',)
    readonly_fields = ('criado_em',)  # Torna o campo 'criado_em' somente leitura
    date_hierarchy = 'criado_em'  # Adiciona uma hierarquia de datas para filtrar

# Registrando as models no admin com as novas funções
admin.site.register(experiencia, ExperienciaAdmin)
admin.site.register(educacao, EducacaoAdmin)
admin.site.register(skills, SkillsAdmin)
admin.site.register(projetos, ProjetosAdmin)
admin.site.register(certificados, CertificadosAdmin)
admin.site.register(contato, ContatoAdmin)
