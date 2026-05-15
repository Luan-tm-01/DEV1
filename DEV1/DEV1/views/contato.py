from django.views import View
from django.shortcuts import render, redirect
from DEV1.forms.contato import ContatoForm

class ContatoView(View):
    @staticmethod
    def get(request):
        formulario = ContatoForm()
        contexto = {
            "formulario": formulario,
            "form_url": "contato_classe"
        }

        return render(request,"contato/contato.html", contexto)
    
    @staticmethod
    def post(request):
        form = ContatoForm(request.POST)
        if form.is_valid():
            assunto = form.cleaned_data.get("assunto")
            remetente = form.cleaned_data.get("remetente")
            mensagem = form.cleaned_data.get("mensagem")
            data = form.cleaned_data.get("data")
            copia = form.cleaned_data.get("copia")
            para = ["contato@restinga.ifrs.edu.br"]

            if copia:
                para.append(remetente)
            
            #send_mail(assunto, mensagem, "sistema@restinga.ifrs.edu.br")

            contexto = {
                "formulario": form,
                "destinatarios": para

            }

        return render(request, "contato/obrigado.html", contexto)