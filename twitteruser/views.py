from django.shortcuts import render, HttpResponseRedirect,reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

from authentication.views import login_view
from twitteruser.models  import TwitterUser
from tweet.models import TweetModel
from twitteruser.forms import SignupForm

# Create your views here.

@login_required
def index(request):
    html = 'index.html'
    latest_tweets = TweetModel.objects.all().order_by('post_date')
    return render(request, html, {"tweets": latest_tweets})

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


def user_detail_view(request, tweet_id):
    html = "user_detail.html"
    my_user = TwitterUser.objects.filter(id=tweet_id).first()
    user_tweets = TweetModel.objects.filter(author=my_user)
    return render(request, html, {'usertweets': user_tweets})
