from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

class PerfilView(LoginRequiredMixin, View):
    raise_exception = True

    @staticmethod
    def get (request):
        contexto = {
            "usuario": request.user,
        }
        return render(request, "contas/perfil.html", contexto)