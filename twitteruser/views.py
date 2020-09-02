from django.shortcuts import render, HttpResponseRedirect,reverse

from authentication.views import login_view
from twitteruser.models  import TwitterUser
from twitteruser.forms import SignupForm
from django.conf import settings
# Create your views here.

def index(request):
    return render(request, "index.html", {"display": settings.AUTH_USER_MODEL})

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = TwitterUser.objects.create_user(
                username=data.get("username"),
                password=data.get("password"),
                displayname=data.get("displayname")
            )
            login_view(request, new_user)
            return HttpResponseRedirect(reverse('homepage'))
    form = SignupForm()
    return render(request, 'basic.html', {"form": form})
