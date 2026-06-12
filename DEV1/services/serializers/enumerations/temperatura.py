from django.db import models

class Temperatura(models.TextChoices):
    CELSIUS = "C", "Celsius"
    FAHRENHEIT = "F", "fahrenheit"
    KELVIN = "K", "Kelvin"