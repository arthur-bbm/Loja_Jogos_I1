from django.db import models

# Create your models here.

class Desenvolvedor(models.Model):
    nome = models.CharField(max_length=128)
    engine = models.CharField(max_length=128)
    data_fundacao = models.DateField()

    def __str__(self):
        return self.nome

class Plataforma(models.Model):
    tipo = models.CharField(max_length=32)
    nome = models.CharField(max_length=128)
    geracao = models.IntegerField(blank=True, null=True)
    ano_lancamento = models.DateField()

class Jogo(models.Model):
    titulo = models.CharField(max_length=128)
    classificacao_indicativa = models.IntegerField()
    estilo = models.CharField(max_length=128)
    genero = models.CharField(max_length=128)
    data_lancamento = models.DateField()
    descricao = models.TextField(blank=True, null=True)

    desenvolvedor = models.ForeignKey(Desenvolvedor, on_delete=models.SET_NULL, null=True)

    plataforma = models.ManyToManyField(Plataforma)

    def __str__(self):
        return self.nome