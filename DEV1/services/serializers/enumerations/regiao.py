from django.db import models

class FreteRegiao(models.TextChoices):
    SUL = "S", "Sul"
    SUDESTE = "SE", "Sudeste"
    CENTRO_OESTE = "CO", "Centro Oeste"
    NORTE = "N", "Norte"
    NORDESTE = "NE", "Nordeste"