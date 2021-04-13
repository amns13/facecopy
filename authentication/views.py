from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.http import require_GET
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, LoginForm


class RegisterView(View):
    form_class = RegisterForm
    template_name = 'authentication/register.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('index'))
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('index'))
        form = self.form_class(request.POST)
        if form.is_valid():
            email = request.POST['email']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            password = make_password(request.POST['password'])
            User.objects.create(email=email,
                                username=email,
                                password=password,
                                first_name=first_name,
                                last_name=last_name)
            return redirect(reverse('login'))


        return render(request, self.template_name, {'form': form})


class LoginView(View):
    form_class = LoginForm
    template_name = 'authentication/login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('index'))
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('index'))
        form = self.form_class(request.POST)
        if form.is_valid():
            username = request.POST['email']
            password = request.POST['password']

            # user = User.objects.filter(username=username)
            # if len(user) == 1 and check_password(password, user[0].password):
            #     login
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return(redirect('index'))

        return render(request, self.template_name, {'form': form})


@require_GET
@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse('login'))