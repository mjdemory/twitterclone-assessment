from django.shortcuts import render, HttpResponseRedirect,reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

from authentication.views import login_view
from twitteruser.models  import TwitterUser
from twitteruser.forms import SignupForm
from django.conf import settings
# Create your views here.

@login_required
def index(request):
    return render(request, "index.html", {"display": settings.AUTH_USER_MODEL})

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = TwitterUser.objects.create_user(
                displayname=data.get("displayname"),
                username=data.get("username"),
                password=data.get("password"),
                )
            login(request, new_user)
            return HttpResponseRedirect(reverse('homepage'))
    form = SignupForm()
    return render(request, 'basic.html', {"form": form})
