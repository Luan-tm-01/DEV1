from aula.forms import Baseform
from aula.models import Pessoa

class PessoaForm(Baseform):
    class Meta:
        model = Pessoa
        fields = "__all__"

