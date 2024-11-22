# Generated by Django 5.1.3 on 2024-11-22 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0004_alter_projetos_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(blank=True, max_length=20)),
                ('mensagem', models.TextField()),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]