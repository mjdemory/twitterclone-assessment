from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from authentication.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get(
                'username'), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("homepage"))
    form = LoginForm()
    return render(request, 'login.html', {"form": form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))