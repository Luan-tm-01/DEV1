from django.db import models

class Operacao(models.TextChoices):
    ADICAO = "+", "Adição"
    SUBTRACAO = "-", "Subtração"
    MULTIPLICAÇÃO = "*", "Multiplicação"
    DIVISAO = "/", "Divisão"
    AND = "&" "E Lógico"
    OR = "|", "OU Lógico"