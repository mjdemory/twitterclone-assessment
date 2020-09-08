from django.shortcuts import render, HttpResponseRedirect,reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


from authentication.views import login_view
from twitteruser.models  import TwitterUser
from tweet.models import TweetModel
from notification.models import Notification
from twitteruser.forms import SignupForm

# Create your views here.

@login_required
def index(request):
    html = 'index.html'
    latest_tweets = TweetModel.objects.filter(author=request.user)
    following_list = TweetModel.objects.filter(author__in=request.user.following.all())
    main_feed = latest_tweets | following_list
    main_feed = main_feed.order_by("-post_date")
    notification_count = Notification.objects.filter(receiver__id=request.user.id, notification_flag=False)
    return render(request, html, {"tweets": latest_tweets, "following_lists": following_list, "main_feed": main_feed, "notification_count": len(notification_count)})


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


# lori code
def follow_view(request, follow_id):
    signed_in_user = TwitterUser.objects.get(username=request.user.username)
    add_user = TwitterUser.objects.filter(id=follow_id).first()
    signed_in_user.following.add(add_user)
    signed_in_user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))




# lori code
def unfollow_view(request, unfollow_id):
    signed_in_user = TwitterUser.objects.get(username=request.user.username)
    remove_user = TwitterUser.objects.filter(id=unfollow_id).first()
    signed_in_user.following.remove(remove_user)
    signed_in_user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))



# def user_detail_view(request, tweet_id):
#     html = "user_detail.html"
#     my_user = TwitterUser.objects.filter(id=tweet_id).first()
#     user_tweets = TweetModel.objects.filter(author=my_user)
#     follow_count = len(my_user.following.all())
#     return render(request, html, {'user_tweets': user_tweets, "current_user": my_user, "follow_count": follow_count})

class user_detail_view(LoginRequiredMixin,TemplateView):
    def get(self, request, tweet_id):
        html = "user_detail.html"
        my_user = TwitterUser.objects.filter(id=tweet_id).first()
        user_tweets = TweetModel.objects.filter(author=my_user)
        follow_count = len(my_user.following.all())
        return render(request, html, {'user_tweets': user_tweets, "current_user": my_user, "follow_count": follow_count})

