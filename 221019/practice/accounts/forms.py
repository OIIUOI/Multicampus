from django.contrib.auth.forms import AuthenticationForm
from ..pjt.settings import AUTH_USER_MODEL

class CustomUserForm(AuthenticationForm):
    class Meta:
        model = AUTH_USER_MODEL
        fields = '__all__'