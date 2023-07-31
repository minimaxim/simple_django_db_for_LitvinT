from django.contrib.auth.forms import AuthenticationForm
from django.forms import CharField, TextInput, PasswordInput


class LoginForm(AuthenticationForm):
    username = CharField(
        max_length=32,
        widget=TextInput(
            attrs={
                'class': 'form-control',
                'type' : 'text',
                'name' : 'name',
                'id' : 'id_name'
            }
        )
    )
    password = CharField(
        min_length=4,
        widget=PasswordInput(
            attrs={
                'class': 'form-control',
                'type': 'password',
                'name': 'password',
                'id': 'id_password'
            }
        )
    )

