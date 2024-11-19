from django.db import models


class experiencia(models.Model):
    data = models.CharField(max_length=100, null=False, blank=False)
    funcao = models.CharField(max_length=100, null=False, blank=False)
    empresa = models.CharField(max_length=100, null=False, blank=False)
    local = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)

    def __str__(self):
        return f"{self.funcao} em {self.empresa}"


class educacao(models.Model):
    data = models.CharField(max_length=100, null=False, blank=False)
    colegio = models.CharField(max_length=100, null=False, blank=False)
    local = models.CharField(max_length=100, null=False, blank=False)
    especialidade = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)

    def __str__(self):
        return f"{self.colegio} - {self.especialidade}"


class skills (models.Model):
    skill = models.CharField(max_length=100, null=False, blank=False)
    def __str__(self):
        return self.skill


class projetos(models.Model):
    nome_projeto = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)
    url_projeto = models.TextField(max_length=100, null=False, blank=False, default="https://github.com/pontesvjp")
    def __str__(self):
        return self.nome_projeto
