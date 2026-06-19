from django.contrib import admin
from .models import Pessoa, Aluno, Passaporte, Reporter

admin.site.register(Pessoa)
admin.site.register(Aluno)
admin.site.register(Passaporte)
admin.site.register(Reporter)
