from django.shortcuts import render, HttpResponseRedirect,reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

from tweet.models import TweetModel
from tweet.forms import TweetForm
from twitteruser.models import TwitterUser

# Create your views here.

@login_required
def create_tweet_view(request):
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            TweetModel.objects.create(
                body=data.get('body'),
                author=request.user,
            )
    
            return HttpResponseRedirect(reverse("homepage"))

    form = TweetForm()
    return render(request, "basic.html", {"form":form})

def tweet_detail_view(request, tweet_id):
        html= 'tweet_detail.html'
        tweet_detail = TweetModel.objects.filter(id=tweet_id).first()
        return render(request, html, {'tweet': tweet_detail})

    