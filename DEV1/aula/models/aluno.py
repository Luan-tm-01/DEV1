from django.db import models
from aula.models import Pessoa
from django.core.validators import MinLengthValidator

class Aluno(Pessoa):
    email = models.EmailField(max_length=255,
        verbose_name='E-mail',
        help_text='E-mail institucional do aluno'
    )

    cod = models.CharField(max_length=10,
                                 validators=[MinLengthValidator(10)],
                                 unique=True,
                                 verbose_name='Matrícula',
                                 help_text="Digite a matrícula do aluno"
                                 )
    
    

    def __str__(self):
        return f'{self.cod} - {self.nome}'
