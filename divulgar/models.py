from django.db import models
from django.contrib.auth.models import User

class Raca(models.Model):
    raca = models.CharField(max_length=30)

    def __str__(self):
        return self.raca

class Tag(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag

class Pet(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    foto = models.ImageField(upload_to="fotos_pets")
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    telefone = models.CharField(max_length=14)
    tags = models.ManyToManyField(Tag) #RELAÇÃO DE MUITOS PRA MUITOS É MANYTOMANYFIELD
    raca = models.ForeignKey(Raca, on_delete=models.DO_NOTHING) #RELAÇÃO DE UM PARA MUITOS É FOREIGNKEY
    choices_status = (('P', 'Para Adoção',),
                        ('A', 'Adotado'))
    status = models.CharField(max_length=1, choices= choices_status)

    def __str__(self):
        return self.nome
    
    