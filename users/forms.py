from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = 'Vaaditaan. Enintään 150 merkkiä. Kirjaimia, numeroita ja merkkejä @/./+/-/_.'
        self.fields['password1'].help_text = '''Salasanasi tulee täyttää seuraavat ehdot:
                                            • Vähintään 8 merkkiä pitkä
                                            • Ei saa olla pelkkiä numeroita
                                            • Ei saa olla liian yleinen
                                            • Ei saa olla sama kuin käyttäjätunnus'''
        self.fields['password2'].help_text = 'Syötä sama salasana uudelleen varmistaaksesi.'
        self.fields['password1'].label = 'Salasana'
        self.fields['password2'].label = 'Salasanan vahvistus'

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Käyttäjätunnus'
        self.fields['password'].label = 'Salasana'