from .models import Persona
from django.contrib.auth.forms import AuthenticationForm

class PersonaLoginForm(AuthenticationForm):
    class Meta:
        model = Persona
        fields = ['email','password']