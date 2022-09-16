from django.db.models import Model, CharField, TextField, IntegerField

# Create your models here.
class Atracao(Model):
    nome = CharField(max_length=150)
    descricao = TextField()
    horario_func = TextField()
    idade_minima = IntegerField()

    def __str__(self):
        return self.nome

