from django.forms import Form, CharField, EmailField, PasswordInput, ValidationError
from django.contrib.auth.models import User


class RegisterForm(Form):
    # All fields are required by default.
    # Username is same as email address
    first_name = CharField(max_length=30, label='First name')
    last_name = CharField(max_length=30, label='Last name')
    email = EmailField(max_length=50, label='Email Address')
    password = CharField(widget=PasswordInput(), label='Select a password')
    repeat_password = CharField(widget=PasswordInput(), label='Repeat password')

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise ValidationError("This email address already exists.")
        return data

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        repeated = cleaned_data.get('repeat_password')

        if password != repeated:
            raise ValidationError("Passwords don't match.")


class LoginForm(Form):
    email = CharField(label='Email')
    password = CharField(widget=PasswordInput(), label='Password')