# Generated by Django 5.1.2 on 2024-11-20 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0002_projetos_url_projeto'),
    ]

    operations = [
        migrations.CreateModel(
            name='certificados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cert', models.CharField(max_length=100)),
                ('nome_cert', models.CharField(max_length=100)),
                ('local_cert', models.CharField(blank=True, max_length=100)),
                ('descricao_cert', models.TextField()),
                ('url_cert', models.CharField(max_length=100)),
            ],
        ),
    ]
