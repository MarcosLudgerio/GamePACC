from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UsuarioCreateForm
from .models import User
from django.contrib.auth.views import LoginView


class ViewCreate(CreateView):
    model = User
    form_class = UsuarioCreateForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('redirect')
    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response




class LoginPersonal(LoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('redirect')


@login_required
def redirect_view(request):
    if request.user.profile == 'instructor':
        return redirect('instructor:dashboard')
    elif request.user.profile == 'player':
        return redirect('player:lobby')
    else:
        return redirect('login')
